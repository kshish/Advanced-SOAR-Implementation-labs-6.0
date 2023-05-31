def list_peers(queryResultData=None, containerID=None, **kwargs):
    """
    Args:
        queryResultData
        containerID
    
    Returns a JSON-serializable object that implements the configured data paths:
        listName
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(containerID)
    phantom.debug(type(containerID))
    list_name = "temp_peer_list_%s" % containerID
    
    # You need the container object in order to update it.
    #update_container = phantom.get_container(containerID)
    
    # Get the data node of the container
    #data = phantom.get_container(containerID)['data']
    #data.update({"peer_list":list_name})
    #phantom.update(update_container, {'data':data} )

    phantom.remove_list(list_name)
    phantom.debug("==================================================")
    phantom.debug(queryResultData)
    phantom.debug("==================================================")

    for host in queryResultData[0]: 
        phantom.add_list(list_name, [host["peer"],host["priority"],host["count"]])
    
    # The actual list is in slot 3 of the tuple returned by phantom.get_list()
    # results_list = phantom.get_list(list_name)[2]
    # phantom.debug(results_list)
    outputs = {"listName": list_name}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
