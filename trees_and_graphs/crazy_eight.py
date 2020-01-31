class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.neighbors = set()

    def add_neighbor(self, card):
        self.neighbors.add(card)

class Hand:
    def __init__(self):
        self.cards = []
        self.distance = {}
        self.links = {}
    
    def add_card(self, number, suit):
        self.cards.append(Card(number, suit))

    def make_graph(self):
        last_non_wild = None
        for i, card in enumerate(self.cards):
            if card.number != 8:
                last_non_wild = card
            for j in range(i+1, len(self.cards)):
                if card.number == 8 or self.cards[j] == 8 or card.number == self.cards[j].number or card.suit == self.cards[j].suit:
                    card.add_neighbor(self.cards[j])
            
                
    def _longest_path(self, graph, vertex):
        if len(vertex.neighbors) == 0:
            self.distance[vertex] = 0
            self.link[vertex] = None

        if node in self.distance:
            return self.distance[node]

        self.distance[vertex] = -float('inf')
        self.link[vertex] = None
        for neighbor in vertex.neighbors:
            new_distance = 1 + self.longest_path(graph, neighbor)
            if new_distance > self.distance[vertex]:
                self.distance[vertex] = new_distance
                self.link[vertex] = neighbor
        return self.distance[vertex]

    
if __name__ == "__main__":
    hand = Hand()
    hand.add_card(4, 'D')
    hand.add_card(8, 'D')
    hand.add_card(5, 'H')
    hand.add_card(5, 'S')
    hand.add_card(7, 'H')
    hand.add_card(9, 'D')

    hand.make_graph()
    hand._longest_path()
