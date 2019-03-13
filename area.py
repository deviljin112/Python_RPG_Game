rooms = {

    "spawn" : {
        "name"  : "Spawn",
        "east"  : 2
    },

    "alley" : {
        
        1   : {
            "name"  : "Alleyway_1",
            "east"  : 2,
            "south" : 3,
            "west"  : 4
        },
        
        2   : {
            "name"  : "Alleyway_2",
            "east"  : 2,
            "west"  : 4
        }
    },

    "house" : {

        1   : {
            "name"  : "Hall",
            "north" : 1,
            "east"  : 2,
            "south" : 3,
            "west"  : 4
        },

        2   : {
            "name"  : "Closet",
            "east"  : 2,
            "enemy" : "Zombie"
        },

        3   : {
            "name"  : "Bedroom",
            "west"  : 4,
            "south" : 3,
            "bed"   : "Bed"
        },

        "living_room"   : {

            1   : {
                "name"  : "Living_Room_1",
                "north" : 1,
                "west"  : 4,
                "south" : 3
            },

            2   : {
                "name"  : "Living_Room_2",
                "east"  : 2,
                "south" : 3,
                "npc"   : "Villager"
            },

            3   : {
                "name"  : "Living_Room_3",
                "north" : 1,
                "east"  : 2,
                "chest" : "Chest"
            },

            4   : {
                "name"  : "Living_Room_4",
                "north" : 1,
                "west"  : 4
            }
        }
    }

}