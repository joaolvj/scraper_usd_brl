import cot

def main():
    try:
        results = cot.display_conversion()
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()