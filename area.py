rooms = {

    "spawn" : {
        "name"      : "Spawn",
        "connects"  : {
            1   : "house"
        }
    },

    "alley" : {
        
        1   : {
            "name"      : "Alleyway_1",
            "connects"  : {
                1   : "spawn",
                2   : "Alleyway_2",
                3   : "Hall"
            }
        },
        
        2   : {
            "name"      : "Alleyway_2",
            "connects"  : {
                1   : "Alleyway_1"
            }
        }
    },

    "house"   : {

        1   : {
            "name"      : "Hall",
            "connects"  : {
                1   : "Alleyway_1",
                2   : "Closet",
                3   : "Bedroom",
                4   : "Living_Room_1"
            }
        },

        2   : {
            "name"      : "Closet",
            "enemy"     : "Zombie",
            "connects"  : {
                1   : "Hall"
            }
        },

        3   : {
            "name"      : "Bedroom",
            "bed"       : "Bed",
            "connects"  : {
                1   : "Hall",
                2   : "Balcony_1"
            }
        },

        "living_room"   : {

            1   : {
                "name"      : "Living_Room_1",
                "connects"  : {
                    1   : "Hall",
                    2   : "Living_Room_2",
                    3   : "Living_Room_4"
                }
            },

            2   : {
                "name"      : "Living_Room_2",
                "npc"       : "Villager",
                "connects"  :   {
                    1   : "Living_Room_1",
                    2   : "Living_Room_3"
                }
            },

            3   : {
                "name"      : "Living_Room_3",
                "chest"     : "Chest",
                "connects"  : {
                    1   : "Living_Room_2",
                    2   : "Living_Room_4"
                }
            },

            4   : {
                "name"      : "Living_Room_4",
                "connects"  : {
                    1   : "Living_Room_1",
                    2   : "Living_Room_3"
                }
            }
        },

        "terrace"       :{
            1   : {
                "name"      : "Balcony_1",
                "connects"  : {
                    1   : "Bedroom",
                    2   : "Balcony_2"
                }
            },

            2   : {
                "name"      : "Balcony_2",
                "connects"  : {
                    1   : "Balcony_1"
                }
            }
        }
    }

}