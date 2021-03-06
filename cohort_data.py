"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    file = open(filename)

    houses = set()

    for line in file:
        line = line.rstrip()
        list_line = line.split('|')
        house = list_line[2]

        if house == "":
            continue
        else:
            houses.add(house)
    
    # TODO: replace this with your code

    return houses




def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
    >>> students_by_cohort('cohort_data.txt')
    ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

    >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
    ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

    >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
    ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

    >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
    ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

    >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
    ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
    - filename (str): the path to a data file
    - cohort (str): optional, the name of a cohort

    Return:
    - list[list]: a list of lists
    """
    file = open(filename)

    students = []
    
    for line in file:
        line = line.rstrip()
        line_list = line.split('|')

        student_name = line_list[0] + " " + line_list[1]
        cohort_name = line_list[4]
      
        if cohort == "All":
            if cohort_name == "I" or cohort_name == "G":
                continue
            else:
                students.append(student_name)

        elif cohort == cohort_name:
            students.append(student_name)

    return sorted(students)

      


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []


    # TODO: replace this with your code

    file = open(filename)

    for line in file:
        line = line.rstrip()
        line_list = line.split('|')

        student_name = line_list[0] + " " + line_list[1]
        house_name = line_list[2]
        cohort_name = line_line[4]

        if house_name == "Dumbledore's Army":
            dumbledores_army.append(student_name)
        elif house_name == "Gryffindor":
            gryffindor.append(student_name)
        elif house_name == "Hufflepuff":
            hufflepuff.append(student_name)
        elif house_name == "Ravenclaw":
            ravenclaw.append(student_name)
        elif house_name == "Slytherin":
            slytherin.append(student_name)
        elif cohort_name == "G":
            ghosts.append(student_name)
        elif cohort_name == "I":
            instructors.append(student_name)

    rosters = [sorted(dumbledores_army),
              sorted(gryffindor),
              sorted(hufflepuff),
              sorted(ravenclaw),
              sorted(slytherin),
              sorted(ghosts),
              sorted(instructors)]

    return rosters


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
