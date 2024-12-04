from enum import Enum
from typing import List, Optional


DATA_SOURCE = "test_data.txt"


class Status(Enum):
    """
    Represents the state of a report.

    Enum Members:
        UNCHECKED (1): The report has not been reviewed.
        UNSAFE (2): The report has been reviewed and is unsafe.
        SAFE (3): The report has been reviewed and is safe.
    """

    UNCHECKED = 1
    UNSAFE = 2
    SAFE = 3


class Report:
    """
    Represents a single report from the Red-Nosed reactor.

    Attributes:
        levels (List[int]): A list of levels that make up a report.
        status (Status): The status of the report.
    """

    def __init__(self, levels: List[int]):
        """
        Construct a new Report.

        Args:
            levels (List[int]): A list of levels that make up the report.
        """
        self.levels: List[int] = levels
        self.status: Status = Status.UNCHECKED

    def determine_status(self):
        """
        Determine wether a report is safe or unsafe.

        Notes:
            - If the levels are not all increasing or decreasing the report is
              unsafe.
            - If the levels differ by less than one or more than three the
              report is unsafe.
        """
        # Initialize logical variables
        i: int = 0
        j: int = 1
        previous_difference: int = 0

        # For each pair in the list
        while j < len(self.levels):
            # Get the difference
            difference = self.levels[j] - self.levels[i]

            # Determine if the pair breaks any rules
            if difference < -3 or difference == 0 or difference > 3:
                self.status = Status.UNSAFE
                return
            if previous_difference < 0 and difference > 0:
                self.status = Status.UNSAFE
                return
            if previous_difference > 0 and difference < 0:
                self.status = Status.UNSAFE
                return

            # Update the logical variables
            i += 1
            j += 1
            previous_difference = difference

        # Set status to safe if there are no failures
        self.status = Status.SAFE

    def is_safe(self) -> bool:
        """
        Used to determine if a report is safe or not.

        Calls determine_status() on the report if status is unchecked.

        Returns:
            (bool): True if the report is safe and False if it is unsafe.
        """
        # Make sure the report is checked
        if self.status == Status.UNCHECKED:
            self.determine_status()

        if self.status == Status.SAFE:
            return True
        else:
            return False

    def determine_dampened_status(self):
        """
        Checks if the levels are safe with dampening.
        """
        if self.status == Status.SAFE:
            return

        for i in range(len(self.levels)):
            levels = self.levels.copy()
            levels.pop(i)
            temp_report = Report(levels)
            if temp_report.is_safe():
                self.status = Status.SAFE
                return


class Data:
    """
    Represents the unusual data.

    Attributes:
        reports (List[Optional[Report]]): A list of all the reports in the
            data.
        total_reports (int): The total number of reports in the data.
        safe_reports (int): The total number of safe reports.
    """

    def __init__(self):
        """
        Construct a new Data object.
        """
        self.reports: List[Optional[Report]] = []
        self.total_reports: int = len(self.reports)
        self.safe_reports: int = 0

    def add_report(self, report: Report):
        """
        Add a Report to the data.

        Args:
            report (Report): The report to be added.
        """
        self.reports.append(report)
        self.total_reports += 1

    def check_reports(self):
        """
        Update the count of safe reports.
        """
        self.safe_reports = 0
        for report in self.reports:
            if report.is_safe():
                self.safe_reports += 1

    def check_reports_with_dampening(self):
        """
        Update the count of safe reports while using dampening.
        """
        self.safe_reports = 0
        for report in self.reports:
            report.determine_dampened_status()
            if report.is_safe():
                self.safe_reports += 1

    def get_safe_reports(self) -> int:
        """
        Get the number of safe reports.

        Returns:
            (int): The number of safe reports.
        """
        return self.safe_reports

    def print_results(self):
        """
        Print the number of safe reports to the console.
        """
        print(f"Safe reports: {self.safe_reports}/{self.total_reports}")
