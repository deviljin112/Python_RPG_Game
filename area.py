rooms = {

    "spawner" : {

        "spawn" : {
            "name"      : "Spawn",
            "connects"  : {
                1   : "alleyway_1"
            }
        }
    },

    "alley" : {
        
        "alleyway_1"   : {
            "name"      : "Alleyway_1",
            "connects"  : {
                1   : "spawn",
                2   : "alleyway_2",
                3   : "hall"
            }
        },
        
        "alleyway_2"   : {
            "name"      : "Alleyway_2",
            "connects"  : {
                1   : "alleyway_1"
            }
        }
    },

    "house"   : {

        "hall"   : {
            "name"      : "Hall",
            "connects"  : {
                1   : "alleyway_1",
                2   : "closet",
                3   : "bedroom",
                4   : "living_room_1"
            }
        },

        "closet"   : {
            "name"      : "Closet",
            "enemy"     : "Zombie",
            "connects"  : {
                1   : "hall"
            }
        },

        "bedroom"   : {
            "name"      : "Bedroom",
            "bed"       : "Bed",
            "connects"  : {
                1   : "hall",
                2   : "balcony_1"
            }
        },

        "living_room"   : {

            "living_room_1"   : {
                "name"      : "Living_Room_1",
                "connects"  : {
                    1   : "hall",
                    2   : "living_Room_2",
                    3   : "living_Room_4"
                }
            },

            "living_room_2"   : {
                "name"      : "Living_Room_2",
                "npc"       : "Villager",
                "connects"  :   {
                    1   : "living_Room_1",
                    2   : "living_Room_3"
                }
            },

            "living_room_3"   : {
                "name"      : "Living_Room_3",
                "chest"     : "Chest",
                "connects"  : {
                    1   : "living_Room_2",
                    2   : "living_Room_4"
                }
            },

            "living_room_4"   : {
                "name"      : "Living_Room_4",
                "connects"  : {
                    1   : "living_Room_1",
                    2   : "living_Room_3"
                }
            }
        },

        "terrace"       :{
            "balcony_1"   : {
                "name"      : "Balcony_1",
                "connects"  : {
                    1   : "bedroom",
                    2   : "balcony_2"
                }
            },

            "balcony_2"   : {
                "name"      : "Balcony_2",
                "connects"  : {
                    1   : "balcony_1"
                }
            }
        }
    }
}