print()
print('*******************************OUTPUT************************************')
def List_Op(Mylist, Mylist2):
    # Write your code here
    print(Mylist,\n,Mylist[0])
if __name__ == '__main__':
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    qw2_count = int(input().strip())

    qw2 = []

    for _ in range(qw2_count):
        qw1_item = int(input().strip())
        qw2.append(qw1_item)

    List_Op(qw1,qw2)





print('*************************************************************************')