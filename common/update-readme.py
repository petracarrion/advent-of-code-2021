import glob
import os


def main():
    lines = ['# Advent of Code 2021', '']

    os.chdir('..')
    files = glob.glob('day**/*.py', recursive=True)
    files = sorted(files)
    files = [file.split('/') for file in files]
    last_file = ['', '']
    for file in files:
        if file[0] != last_file[0]:
            lines.append(f'* [{file[0]}]({file[0]})')
        lines.append(f'    * [{file[1]}]({file[0]}/{file[1]})')
        last_file = file

    with open('README.md', 'w') as f:
        for line in lines:
            f.write("%s\n" % line)


if __name__ == '__main__':
    main()
