def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    :param boxes: A list of lists where each sublist contains keys to other boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    # Track which boxes have been opened (box 0 is open by default)
    opened = set([0])
    # Use a stack (or list) to hold keys that we find
    keys = [0]  # Start with the key to box 0
    
    while keys:
        current_key = keys.pop()  # Get the most recent key (DFS approach)
        
        # Try to unlock the box corresponding to current_key
        for key in boxes[current_key]:
            if key not in opened and key < len(boxes):  # Valid key to unlock a box
                opened.add(key)  # Mark the box as unlocked
                keys.append(key)  # Add new keys to unlock other boxes
    
    # Check if all boxes are unlocked
    return len(opened) == len(boxes)
