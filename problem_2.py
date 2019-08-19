import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_suffix_files = []
    list_suffix_files = recursive_find_files(suffix, path, list_suffix_files)
    return list_suffix_files

def recursive_find_files(suffix, path, paths_suffix):
   if os.path.isfile(path):
      if path.endswith(suffix):
         return [path]
      else:
         return None
   if os.path.isdir(path):
      found_path = []
      possibles_paths = os.listdir(path)
      for path_name in possibles_paths:
         smart_path = os.path.join(path, path_name)
         file = recursive_find_files(suffix, smart_path, paths_suffix)
         if file != None:
            found_path = found_path + file
      return found_path
    
def test_dir():
   result = find_files(".h", "/testdir")
   print(result)

def test_search_py():
   result = find_files(".py", "./")
   print(result)

def test_search_md():
   result = find_files(".md", "./")
   print(result)

def test_search_avi():
   result = find_files(".avi", "./")
   print(result)

test_dir()
test_search_py()
test_search_md()
test_search_avi()