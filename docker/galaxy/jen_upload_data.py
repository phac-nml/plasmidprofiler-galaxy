#!/usr/bin/env python
import argparse
from bioblend import galaxy                   
import time     


def main(api_key, api_url,import_file,library_name):

    gi = galaxy.GalaxyInstance(url=api_url, key=api_key)        

    library_id=None
    
    #check to see if the library exists 
    library_info = gi.libraries.get_libraries(name=library_name)

    #if exists, then upload file there
    if library_info:
        #always get the first result if there is more then data library with the same name
        library_info = library_info[0]
        library_id = library_info['id']
    else:
        library_info = gi.libraries.create_library(name=library_name)
        library_id = library_info['id']
        #create new libray


    results = gi.libraries.upload_file_from_local_path(library_id,import_file)
    if 'id' in results[0]:
        print "Succesfully added '%s' with dataset id '%s' in library '%s' at root folder level" % (results[0]['name'],results[0]['id'],library_name)
    else:
        print "Failed to add file '%s' in library '%s'" % (import_file,library_name)


    debuginfo = gi.libraries.show_dataset(library_id,results[0]['id'])

    while (debuginfo['state'] == "queued"):
        debuginfo = gi.libraries.show_dataset(library_id,results[0]['id'])
    
    print "dataset info: '%s'" %(debuginfo['state'])
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog="Script is to upload a single file into the root folder of a data library. \nWill create new data library if none is found with name provided. \nPlease give full path of the file to be uploaded.")
    
    parser.add_argument('--api_key', action="store", dest="api_key",required=True,help='Your API key from Galaxy')
    parser.add_argument('--api_url', action="store", dest="api_url",required=True,help='Url of the Galaxy instance to submit your request to. i.e: http://localhost:8080')
    parser.add_argument('--import_file', action="store", dest="import_file",required=True,help='Full path of file to be imported')
    parser.add_argument('--library_name', action="store", dest="library_name",required=True)
    args = parser.parse_args()
    #take the args out of the namespace and into a dictionary
    dic = vars(args)
    

        
    main(**dic)    
