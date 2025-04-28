import pygame
import CardFunctions as c
import Token

SCREEN_WIDTH = 1270
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

#Load the board images
def board_images(index):
    go_img = pygame.image.load('resources/gameboard-detail/go.png').convert_alpha()
    the_old_creed_img = pygame.image.load('resources/property_cards_details/property card1.png').convert_alpha()
    pot_luck_img = pygame.image.load('resources/gameboard-detail/Pot Luck.png').convert_alpha()
    gangsters_paradise_img = pygame.image.load('resources/property_cards_details/property card2.png').convert_alpha()
    income_tax_img = pygame.image.load('resources/gameboard-detail/Income Tax.png').convert_alpha()
    brighton_station_img = pygame.image.load('resources/property_cards_details/property card3.png').convert_alpha()
    the_angels_delight_img = pygame.image.load('resources/property_cards_details/property card4.png').convert_alpha()
    opportunity_knocks_img = pygame.image.load('resources/gameboard-detail/Opportunity Knocks.png').convert_alpha()
    potter_avenue_img = pygame.image.load('resources/property_cards_details/property card5.png').convert_alpha()
    granger_drive_img = pygame.image.load('resources/property_cards_details/property card6.png').convert_alpha()
    jail_img = pygame.image.load('resources/gameboard-detail/Jail.png').convert_alpha()
    skywalker_drive_img = pygame.image.load('resources/property_cards_details/property card7.png').convert_alpha()
    tesla_power_co_img = pygame.image.load('resources/property_cards_details/property card8.png').convert_alpha()
    wookie_hole_img = pygame.image.load('resources/property_cards_details/property card9.png').convert_alpha()
    rey_lane_img = pygame.image.load('resources/property_cards_details/property card10.png').convert_alpha()
    hove_station_img = pygame.image.load('resources/property_cards_details/property card11.png').convert_alpha()
    bishop_drive_img = pygame.image.load('resources/property_cards_details/property card12.png').convert_alpha()
    dunham_street_img = pygame.image.load('resources/property_cards_details/property card13.png').convert_alpha()
    broyles_lane_img = pygame.image.load('resources/property_cards_details/property card14.png').convert_alpha()
    free_parking_img = pygame.image.load('resources/gameboard-detail/Free Parking.png').convert_alpha()
    yue_fei_square_img = pygame.image.load('resources/property_cards_details/property card15.png').convert_alpha()
    #opportunity_knocks
    mulan_rouge_img = pygame.image.load('resources/property_cards_details/property card16.png').convert_alpha()
    han_xin_gardens_img = pygame.image.load('resources/property_cards_details/property card17.png').convert_alpha()
    falmer_station_img = pygame.image.load('resources/property_cards_details/property card18.png').convert_alpha()
    shatner_close_img = pygame.image.load('resources/property_cards_details/property card19.png').convert_alpha()
    picard_avenue_img = pygame.image.load('resources/property_cards_details/property card20.png').convert_alpha()
    edison_water_img = pygame.image.load('resources/property_cards_details/property card21.png').convert_alpha()
    crusher_creek_img = pygame.image.load('resources/property_cards_details/property card22.png').convert_alpha()
    go_to_jail_img = pygame.image.load('resources/gameboard-detail/Go to jail.png').convert_alpha()
    sirat_mews_img = pygame.image.load('resources/property_cards_details/property card23.png').convert_alpha()
    ghengis_crescent_img = pygame.image.load('resources/property_cards_details/property card24.png').convert_alpha()
    ibis_close_img = pygame.image.load('resources/property_cards_details/property card25.png').convert_alpha()
    portslade_station_img = pygame.image.load('resources/property_cards_details/property card26.png').convert_alpha()
    james_webb_way_img = pygame.image.load('resources/property_cards_details/property card27.png').convert_alpha()
    super_tax_img = pygame.image.load('resources/gameboard-detail/Super Tax.png').convert_alpha()
    turing_heights_img = pygame.image.load('resources/property_cards_details/property card28.png').convert_alpha()

    board_image = [go_img, the_old_creed_img, pot_luck_img, gangsters_paradise_img, income_tax_img, brighton_station_img, the_angels_delight_img, opportunity_knocks_img,
                   potter_avenue_img, granger_drive_img, jail_img, skywalker_drive_img, tesla_power_co_img, wookie_hole_img, rey_lane_img, hove_station_img, bishop_drive_img, pot_luck_img,
                   dunham_street_img, broyles_lane_img, free_parking_img, yue_fei_square_img, opportunity_knocks_img, mulan_rouge_img, han_xin_gardens_img, falmer_station_img, shatner_close_img,
                   picard_avenue_img, edison_water_img, crusher_creek_img, go_to_jail_img, sirat_mews_img, ghengis_crescent_img, pot_luck_img, ibis_close_img, portslade_station_img,
                   opportunity_knocks_img, james_webb_way_img, super_tax_img, turing_heights_img]

    return board_image[index]

#Create board instances
def game_board():
    go = c.card("go", -1, -1, -1, "Bank", -1, -1, False, 0)
    the_old_creek = c.card("The Old Creek", "Brown", 60, 50, "Bank", [2, 10, 30, 90, 160, 250], 0, False, 1)
    pot_luck = c.card("Pot Luck", -1, -1, -1, "Bank", -1, -1, False,0)
    gangsters_paradise = c.card("Gangsters Paradise", "Brown", 60, 50, "Bank", [4, 20, 60, 180, 320, 450], 0, False, 3)
    income_tax = c.card("Income Tax", -1, -1, -1, "Bank",-1, -1, False, 0)
    brighton_station = c.card("Brighton Station", "Railroad", 200, -1, "Bank", -1, -1, False, 5)
    the_angels_delight = c.card("The Angels Delight", "Blue", 100, 50, "Bank", [6, 30, 90, 270, 400, 550], 0, False, 6)
    opportunity_knocks = c.card("Opportunity Knocks",-1,-1,-1,"Bank", -1, -1, False,0)
    potter_avenue = c.card("Potter Avenue", "Blue", 100, 50, "Bank", [6, 30, 90, 270, 400, 550], 0, False, 8)
    granger_drive = c.card("Granger Drive", "Blue", 120, 50, "Bank", [8, 40, 100, 300, 450, 600], 0, False, 9)
    # new row
    jail = c.card("Visiting Jail", -1, -1, -1 , "Bank",-1, -1, False, 0)
    skywalker_drive = c.card("Skywalker Drive", "Purple", 140, 100, "Bank", [10, 50, 150, 450, 625, 750], 0, False, 11)
    tesla_power_co = c.card("Tesla Power Co", "Utilities", 150, -1, "Bank", -1, -1, False, 12)
    wookie_hole = c.card("Wookie Hole", "Purple", 140, 100, "Bank", [10, 50, 150, 450, 625, 750], 0, False, 13)
    rey_lane = c.card("Rey Lane", "Purple", 160, 100,"Bank", [12, 60, 180, 500, 700, 900], 0, False, 14)
    hove_station = c.card("Hove Station", "Railroad", 200, -1, "Bank", -1, -1, False, 15)
    bishop_drive = c.card("Bishop Drive", "Orange", 180, 100, "Bank", [14, 70, 200, 550, 750, 950], 0, False, 16)
    # pot luck
    dunham_street = c.card("Dunham Street", "Orange", 180, 100, "Bank", [14, 70, 200, 550, 750, 950], 0, False, 18)
    broyles_lane = c.card("Broyles Lane", "Orange", 200, 100, "Bank", [16, 80, 220, 600, 800, 1000], 0, False, 19)
    free_parking = c.card("Free Parking", -1, -1, -1, "Bank", 0, -2, False, 0)
    # rotate
    yue_fei_square = c.card("Yue Fei Square", "Red", 220, 150, "Bank", [18, 90, 250, 700, 875], 0, False, 21)
    # opportunity knocks
    mulan_rouge = c.card("Mulan Rouge", "Red", 220, 150, "Bank", [18, 90, 250, 700, 875, 1050],0, False, 23)
    han_xin_gardens = c.card("Han Xin Gardens", "Red", 240, 150, "Bank", [20, 100, 300, 750, 925, 1100], 0, False, 24)
    falmer_station =c.card("Falmer Station", "Railroad", 200, -1, "Bank", -1, -1, False, 25)
    shatner_close = c.card("Shatner Close", "Yellow", 260, 150, "Bank", [22, 110, 330, 800, 975, 1150], 0, False, 26)
    picard_avenue = c.card("Picard Avenue", "Yellow", 260, 150, "Bank", [22, 110, 330, 800, 975, 1150], 0, False, 27)
    edison_water = c.card("Edison Water", "Utilities", 150, -1, "Bank", -1, -1, False, 28)
    crusher_creek = c.card("Crusher Creek", "Yellow", 280, 150, "Bank", [24, 120, 360, 850, 1025, 1200], 0, False, 29)
    # rotate
    go_to_jail = c.card("Go to Jail", -1, -1, -1,  "Bank", -1, -1, False, 0)
    sirat_mews = c.card("Sirat Mews", "Green", 300, 200,  "Bank", [26, 130, 390, 900, 1100, 1275], 0, False, 31)
    ghengis_crescent = c.card("Ghengis Crescent", "Green", 140, 200, "Bank", [26, 130, 390, 900, 1100, 1275], 0, False, 32)
    # pot luck
    ibis_close = c.card("Ibis Close", "Green", 300, 200, "Bank", [28, 150, 450, 1000, 1200, 1400], 0, False, 34)
    portslade_station = c.card("Short Line", "Railroad", 200, "-1", "Bank", -1, -1, False, 35)
    # opportunity knocks
    james_webb_way = c.card("James Webb Way", "Deep Blue", 350, 200, "Bank", [35, 175, 500, 1100, 1300, 1500], 0, False, 37)
    super_tax = c.card("Super Tax", -1, -1, -1, "Bank", -1, -1, False, 0)
    turing_heights = c.card("Turing Heights", "Deep Blue", 400, 200, "Bank", [50, 200, 600, 1400, 1700, 2000], 0, False, 39)


    board = [
        go,
        the_old_creek,
        pot_luck,
        gangsters_paradise,
        income_tax,
        brighton_station,
        the_angels_delight,
        opportunity_knocks,
        potter_avenue,
        granger_drive,
        jail,
        skywalker_drive,
        tesla_power_co,
        wookie_hole,
        rey_lane,
        hove_station,
        bishop_drive,
        pot_luck,
        dunham_street,
        broyles_lane,
        free_parking,
        yue_fei_square,
        opportunity_knocks,
        mulan_rouge,
        han_xin_gardens,
        falmer_station,
        shatner_close,
        picard_avenue,
        edison_water,
        crusher_creek,
        go_to_jail,
        sirat_mews,
        ghengis_crescent,
        pot_luck,
        ibis_close,
        portslade_station,
        opportunity_knocks,
        james_webb_way,
        super_tax,
        turing_heights
    ]

    return board