class myException(Exception):
    pass

def wellBrackated(exp):
    try:
        if type(exp) != str:
            raise myException
        l = []
        for i in exp:
            if i in ['(', '{', '[']:
                l.append(i)
            else:
                if not l:
                    check = False
                c = l.pop()
                if c == '(' and i != ')':
                    check = False
                if c == '{' and i != '}':
                    check = False
                if c == '[' and i != ']':
                    check = False
        if len(l) == 0:
            check = True
        else:
            check = False
    except myException as e:
        print("Not a string")
        check = False
    except IndexError as g:
        print("List is empty")
        check = False        
    finally:
        print("Done!")
        return check

def rotateList(l, n=0):
    try:
        if type(l) != list:
            raise TypeError
        if len(l) == 0:
            raise IndexError
        if n >= len(l):
            raise myException
        if n > 0:
            return l[len(l)-n:] + l[:len(l)-n]
        if n < 0:
            return l[abs(n):] + l[:abs(n)]
    except TypeError as t:
        print("Not a list")
    except IndexError as i:
        print("List is empty")
    except myException as e:
        print('Number of rotations must be less than total elements')
        return l
    finally:
        print("Done!")

if __name__ == "__main__":
    s = input("Enter expression: ")
    print(wellBrackated(s))
    l = eval(input("Enter List: "))
    n = int(input("Enter number of rotations (0 by default): "))
    print(rotateList(l, n))