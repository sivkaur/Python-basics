def stack(originalList, operation, value = None):
    
    if operation.lower() == 'add' and value is not None:
        originalList.append(value)
    elif operation.lower() == 'remove':
        if len(originalList) == 0:
            print("Stack is empty!")
            return originalList
        originalList.pop()
    else:
        return originalList
        
    return originalList 

def queue(originalList,operation, value = None):
    
    if operation.lower() == 'add' and value is not None:
        originalList.append(value)
    elif operation.lower() == 'remove':
        if len(originalList) == 0:
            print("Queue is empty!")
            return originalList
        originalList.pop(0)
    else:
        return originalList
        
    return originalList 

print("----------------")
print("Stack operations")
print("----------------")
original_stack = []
print("Original Stack: " + str(original_stack))
for i in range(2):
    print("Adding " + str(i) +" to the stack")
    original_stack = stack(original_stack, "add", i)
    print("Updated Stack: " + str(original_stack))
    print()
print("Adding no new value to the stack")
original_stack = stack(original_stack, "add")
print("Updated Stack: " + str(original_stack))
print()
for i in range(3):
    print("Removing an element to the stack")
    Updated_stack = stack(original_stack, "remove")
    print("Updated Stack: " + str(Updated_stack))
    print()

print()

print("----------------")
print("Queue operations")
print("----------------")
original_queue = []
print("Original Queue: " + str(original_queue))
for i in range(2):
    print("Adding " + str(i) +" to the Queue")
    original_queue = queue(original_queue, "add", i)
    print("Updated Queue: " + str(original_queue))
    print()
print("Adding no new value to the Queue")
original_queue = queue(original_queue, "add")
print("Updated Queue: " + str(original_queue))
print()
for i in range(3):
    print("Removing an element to the Queue")
    Updated_queue = queue(original_queue, "remove")
    print("Updated Queue: " + str(Updated_queue))
    print()
