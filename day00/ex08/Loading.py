def ft_tqdm(lst: range) -> None:
    """Prints a progress bar for a given range."""
    for elem in lst:
        percentage = (elem + 1) / lst.stop * 100
        bar = "█" * int(percentage) + " " * (100 - int(percentage))
        print(f"\r{int(percentage)}%|{bar}| {elem + 1}/{lst.stop}", end="")
        yield elem
    print()
