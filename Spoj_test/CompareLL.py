class Node:
    def __init__(self, nodeValue):
        self.data = nodeValue
        self.next = None

#do not change anything above This
def Compare(list1 ,list2):
    temp1=list1
    num1=""
    while(temp1!=None):
        num1+=str(temp1.data)
        temp1=temp1.next
    temp2=list2
    num2=""
    while(temp2!=None):
        num2+=str(temp2.data)
        temp2=temp2.next
    if int(num1)>int(num2):
        return 1
    elif int(num1)<int(num2):
        return -1
    else:
        return 0
    
    
#do not change anything below this



def buildListFromArray(givenArray):

    numElements = len(givenArray)
    if numElements == 0:
        return None
    head = Node(givenArray[0])
    prevNode = head
    for index in range(1, numElements):
        newNode = Node(givenArray[index])
        prevNode.next = newNode
        prevNode = newNode
    return head

if __name__ == '__main__':

    numTest = int(input())

    for i in range(numTest):

        n, m = map(int, input().split())

        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        head1, head2 = buildListFromArray(arr1), buildListFromArray(arr2)


        flag = Compare(head1, head2)

        print(flag)