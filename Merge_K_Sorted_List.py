import heapq

#Definition for singly-linked list
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap= []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
            print(f"Pushing node with value {node.val} from list {i} to heap")

    dummy = ListNode()
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        print(f"Popping node with value {val} from list {i} from heap")
        curr.next = ListNode(val)
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            print(f"Pushing next node with value {node.next.val} from list {i} to heap")

    return dummy.next

#Helper function to create a linked list from python list
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr: 
        curr.next = ListNode(num)
        print(f"Creating node with value: {num}")
        curr = curr.next
        print(f"Current linked list: {dummy.next}")
    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(" -> ".join(map(str, vals)))






if __name__ == "__main__":
    #Create example input (3 sorted lists)
    l1 = create_linked_list([1, 4, 5])
    print("linked list 1 created: {l1}")

    l2 = create_linked_list([1, 3, 4])
    print("linked list 2 created: {l2}")

    lists = [l1, l2]

    merged_head = mergeKLists(lists)

    print("Merged linked list:")
    print_linked_list(merged_head)


    