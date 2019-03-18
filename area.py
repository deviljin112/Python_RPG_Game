rooms = {

    "spawner" : {

        "spawn" : {
            "name"      : "Spawn",
            "interact"  : "",
            "connects"  : {
                1   : "alleyway_1"
            }
        }
    },

    "alley" : {
        
        "alleyway_1"   : {
            "name"      : "Alleyway 1",
            "interact"  : "",
            "connects"  : {
                1   : "spawn",
                2   : "alleyway_2",
                3   : "hall"
            }
        },
        
        "alleyway_2"   : {
            "name"      : "Alleyway 2",
            "interact"  : "",
            "connects"  : {
                1   : "alleyway_1"
            }
        }
    },

    "house"   : {

        "hall"   : {
            "name"      : "Hall",
            "interact"  : "",
            "connects"  : {
                1   : "alleyway_1",
                2   : "closet",
                3   : "bedroom",
                4   : "living_room_1"
            }
        },

        "closet"   : {
            "name"      : "Closet",
            "interact"  : "Zombie",
            "connects"  : {
                1   : "hall"
            }
        },

        "bedroom"   : {
            "name"      : "Bedroom",
            "interact"  : "Bed",
            "connects"  : {
                1   : "hall",
                2   : "balcony_1"
            }
        }
    },

    "living_room"   : {

        "living_room_1" : {
            "name"      : "Living Room 1",
            "interact"  : "",
            "connects"  : {
                1   : "hall",
                2   : "living_room_2",
                3   : "living_room_4"
            }
        },

        "living_room_2" : {
            "name"      : "Living Room 2",
            "interact"  : "Villager",
            "connects"  :   {
                1   : "living_room_1",
                2   : "living_room_3"
            }
        },

        "living_room_3" : {
            "name"      : "Living Room 3",
            "interact"  : "Chest",
            "connects"  : {
                1   : "living_room_2",
                2   : "living_room_4"
            }
        },

        "living_room_4" : {
            "name"      : "Living Room 4",
            "interact"  : "",
            "connects"  : {
                1   : "living_room_1",
                2   : "living_room_3"
            }
        }
    },

    "terrace"       : {

        "balcony_1"     : {
            "name"      : "Balcony 1",
            "interact"  : "",
            "connects"  : {
                1   : "bedroom",
                2   : "balcony_2"
            }
        },

        "balcony_2"     : {
            "name"      : "Balcony 2",
            "interact"  : "",
            "connects"  : {
                1   : "balcony_1"
            }
        }
    }
}