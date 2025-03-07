import MetaTrader5 as mt5

class MetaTrader:
    def __init__(self, path, server, user, password):
        self.path = path
        self.server = server
        self.user = user
        self.password = password

    # Refactor: bring whole login here for just one account
    def Login(self) -> bool:
        try:
            if mt5.terminal_info() is not None:
                return True

            print(f"try to login to {self.server} with {self.user}")
            # establish connection to the MetaTrader 5 terminal
            if not mt5.initialize(path=self.path, login=self.user, server=self.server, password=self.password):
                print("MetaTrader Login failed, error code =",
                             mt5.last_error())
                return False
            print(f"login was successful for {self.user}")
            return True
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
        
    def get_open_positions(self, ticket_id=None, symbol=None):
        """Get open positions from MetaTrader"""
        if ticket_id is not None:
            positions = mt5.positions_get(ticket=ticket_id)
            if (len(positions) == 0):
                # logger.error(f"Can't find position {ticket_id}")
                return None
            return positions[0]
        elif symbol is not None:
            positions = mt5.positions_get(symbol=symbol)
            if (len(positions) == 0):
                # logger.error(f"Can't find position {ticket_id}")
                return None
            return positions
        else:
            positions = mt5.positions_get()

        return list(positions) if positions else []
    
    def shutdown():
        mt5.shutdown()