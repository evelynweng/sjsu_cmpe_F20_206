class Find_to_mac():
    def find_mac(self, to_label):
      
        # import connection
        # only connection now eve<->evelyn<->kitty
        link_config = []
        '''
        with open("configure_of_conneciton.txt") as configure_of_conneciton:
            for line in configure_of_conneciton:
                s = line.split(",")
                link_config.append((s[0], s[1][:-1]))  # endl at the end
        '''
        to_mac = "13.52.77.84"
        #to_mac = "127.0.0.1"
        return to_mac