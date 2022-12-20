class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        keys.add(0)
        visting_room = set()
        to_visit = [0]
        while to_visit:
            visting_room.add(to_visit[0])
            for x in rooms[to_visit[0]]:
                keys.add(x)
                if x not in visting_room:
                    to_visit.append(x)
            to_visit.pop(0)
        return len(rooms)== len(visting_room)
                    
            
        
                    
        
        