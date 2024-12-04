from objects import Data, Report


DATA_FILE_NAME = "data.txt"


def get_data_from(file_name: str) -> Data:
    """
    Load the data from a file into a data structure.

    Args:
        file_name (str): The name of the file containing the data.

    Returns:
        (Data): A data structure containing all the file's data
    """
    data = Data()

    with open(file_name, "r") as file:
        for line in file:
            levels = [int(s) for s in line.strip().split()]
            report = Report(levels)
            data.add_report(report)

    return data


def main():
    """
    The main loop of the program.

    Loads the data from a file into a data structure. Checks each report to see
    if it is safe or not. Prints the number of safe reports.
    """
    data = get_data_from(DATA_FILE_NAME)
    data.check_reports_with_dampening()
    data.print_results()


if __name__ == "__main__":
    main()
