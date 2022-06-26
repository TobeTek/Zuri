from uuid import uuid4

def generate_random_id() -> str:
    """
    A function that generates a random 8 character string. 
    Useful for creating random IDs for URLs and objects.
    """
    # Generate ID
    id = str(uuid4())
    
    # Get the first 8 characters of the id
    id = id[:8]
    
    return id
