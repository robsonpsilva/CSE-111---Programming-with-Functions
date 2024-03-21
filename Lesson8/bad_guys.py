
bad_guys = {'daredevil':'kingpin',
            'x-men': 'apocalypse',
            'batman': 'bane'}

def main():
    print(bad_guys['batman'])

    bad_guys['deadpool'] = 'evil deadpool' #Adding a new pair key-word in dictionary
    print(bad_guys)

    bad_guys['x-men'] = 'juggernaut'
    print(bad_guys)

    del bad_guys['x-men']
    print(bad_guys)

if __name__ == "__main__":
    main()