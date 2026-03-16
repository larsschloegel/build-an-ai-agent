from functions.get_files_info import get_files_info


def test(title, result):
    print(title)
    for line in result.split("\n"):
        print(f"  {line}")
    print()


if __name__ == "__main__":
    result = get_files_info("calculator", ".")
    test("Result for current directory:", result)

    result = get_files_info("calculator", "pkg")
    test("Result for 'pkg' directory:", result)

    result = get_files_info("calculator", "/bin")
    test("Result for '/bin' directory:", result)

    result = get_files_info("calculator", "../")
    test("Result for '../' directory:", result)
