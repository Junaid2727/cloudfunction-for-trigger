import functions_framework


# CloudEvent function to be triggered by an Eventarc Cloud Audit Logging trigger
# Note: this is NOT designed for second-party (Cloud Audit Logs -> Pub/Sub) triggers!
@functions_framework.cloud_event
def my_cloud_function(cloudevent):
    
    # Extracting cloud event data. 
    payload = cloudevent.data.get("protoPayload", {})
    
    # Extracting meta data.
    metadata = payload.get('metadata', {})
    
    # If meta data found continue. 
    if metadata:
        
        # Checking meta data for table change action.
        table_data_change = metadata.get('tableDataChange')
        
        
        if table_data_change:

            # do your logic that was being duplicated before.
            print("HELLO WORLD.")

        else: 
            pass
