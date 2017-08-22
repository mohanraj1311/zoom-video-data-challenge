'''
Question 2
===========

There are few important things to consider while solving this question:

1. Since the server log file is large , one must not attempt to load
the entire file into memory. If an attempt to load the entire file is made,
the system shall crash.

Method to overcome 1:
---------------------
Read the file line by line.
That is, just read and process only 1 line at a time.


2. The file should be loaded to a filesystem or database in a performant way.
The final goal of the server log processing is to gather insights at the end
of the pipeline.

Method to accomplish 2:
------------------------
After reading and parsing , we store the data in Amazon Elastic search.
We can choose Elastic search as its very fast
in searching among millions of records because of its lucene based indexing.

Another advantage of using it is having "drill-down" property which can be very
handy for even non-engineers to analyse the data stored.
Apart from that, it has inbuit support for kibana dashboard which might help
in creating good visualization for the events occuring.

So, we can create an Elastic search "index" say "server_logs".
This index can contain "types" where each type corresponds to the "event-type" in
our log.

Analogy of relational database and elastic search is as follows:


    MySQL => Databases => Tables => Columns/Rows
    Elasticsearch => Indices => Types => Documents with Properties

3. Build in checks for reducing job errors:

Since we are using Elastic search , it becomes easier to acheive this.
Since each event-type correspornds to a particular 'type' in elastic search,
there is no question of creating a new 'type' for a previously recorded event-type,
the elastic search itself shall block it.
Also, while a creating a new 'type' in elastic search, we get the freedom of
defining the "properties of Document" as each document or record shall reside
in the "type".

So, even if 1 record has some irrelvant data or erroneous data, that will not
be part of the documents present in a "type"


Psedocode:

'''
Elasticsearch_index = 'server_logs'

def read_parse_file(filename):
    with open(filename, 'r') as filehandle:
        while(True):
            line = filehandle.readLine()
            if not line:
                break
            else:
                list_of_values = line.split(",")
                event = list_of_values[2]
                store_into_elastic_search(Elasticsearch_index, event, list_of_values)

def store_into_elastic_search(Elasticsearch_index, event, list_of_values):
    if check_event_type_exists_in_index(Elasticsearch_index, event):
        put_record_to_elastic_search(Elasticsearch_index, event, list_of_values)
    else:
        if create_new_type(Elasticsearch_index, event):
            put_record_to_elastic_search(Elasticsearch_index, event, list_of_values)


def check_event_type_exists_in_index(Elasticsearch_index, event):
    if type_exists(Elasticsearch_index, event):
        return True
    else:
        return False

def create_new_type(Elasticsearch_index, type):
    properties = read_config_properties(Elasticsearch_index, type)
    if create_new_type_inbuilt_function(properties, Elasticsearch_index, type):
        return True
    else:
        return False


def put_record_to_elastic_search(Elasticsearch_index, event, list_of_values):
    put_record_to_elastic_search_inbuilt_function(Elasticsearch_index, event, list_of_values)
    return
