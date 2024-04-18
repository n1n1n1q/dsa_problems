def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = node
            while slow != fast:
                slow = slow.next
                fast = fast.next
            res = 1
            start_point = slow
            while slow.next is not start_point:
                res += 1
                slow = slow.next
            return res
    return None
