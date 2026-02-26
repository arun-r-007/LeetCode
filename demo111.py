import collections

servers = collections.deque([
    {"id": "Server_A", "is_up": True, "connections": 0},
    {"id": "Server_B", "is_up": True, "connections": 0},
    {"id": "Server_C", "is_up": False, "connections": 0} 
])

def handle_request(request_data):

    if not any(s['is_up'] for s in servers):
        return "REJECTED: No servers available"

    attempts = 0
    while attempts < len(servers):
        current_server = servers[0]
        servers.rotate(-1) 
        attempts += 1

        if not current_server['is_up']:
            print(f"Skipping {current_server['id']}... it's down.")
            continue

        try:
            #rh
            current_server['connections'] += 1
            print(f"Assigning request to {current_server['id']} (Active: {current_server['connections']})")
            
            #p
            if current_server['id'] == "Server_B":
                raise Exception("Network Timeout")

            return f"SUCCESS: Handled by {current_server['id']}"

        except Exception as e:
            print(f"Error on {current_server['id']}: {e}")
            current_server['is_up'] = False 
            print(f"Retrying next server...")
            

    return "REJECTED: All retries failed"


print(handle_request("Sample Data"))
