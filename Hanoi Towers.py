def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f'Move disk 1 from peg {source} to peg {target}')
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f'Move disk {n} from peg {source} to peg {target}')
    hanoi(n - 1, auxiliary, target, source)

# Test the function
hanoi(4, 'A', 'C', 'B')
