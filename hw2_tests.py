import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = data.Point(8,4)
        point2 = data.Point(2,2)
        self.assertEqual(hw2.create_rectangle(point1,point2),data.Rectangle(data.Point(2,4), data.Point(8,2)))

    def test_create_rectangle2(self):
        point1 = data.Point(-3,1)
        point2 = data.Point(0,8)
        self.assertEqual(hw2.create_rectangle(point1,point2),data.Rectangle(data.Point(-3,8), data.Point(0,1)))
    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = data.Duration(2, 30)
        duration2 = data.Duration(2, 32)
        self.assertEqual(hw2.shorter_duration_than(duration1, duration2), True)

    def test_shorter_duration_than2(self):
        duration1 = data.Duration(3, 2)
        duration2 = data.Duration(2, 58)
        self.assertEqual(hw2.shorter_duration_than(duration1, duration2), False)

    # Part 3
    def test_song_shorter_than1(self):
        song1 = data.Song("singer A", "Track A", data.Duration(2,50))
        song2 = data.Song("singer B", "Track B", data.Duration(3, 57))
        song3 = data.Song("singer C", "Track C", data.Duration(0, 59))
        song4 = data.Song("singer D", "Track D", data.Duration(4, 20))
        song = data.Song("singer E", "Track E", data.Duration(4, 0))
        songlist = [song1, song2, song3, song4]
        self.assertEqual(hw2.song_shorter_than(songlist, song), [song1, song2, song3])

    def test_song_shorter_than2(self):
        song1 = data.Song("singer A", "Track A", data.Duration(3, 12))
        song2 = data.Song("singer B", "Track B", data.Duration(3, 52))
        song3 = data.Song("singer C", "Track C", data.Duration(3, 14))
        song4 = data.Song("singer D", "Track D", data.Duration(0, 20))
        song = data.Song("singer E", "Track E", data.Duration(3, 14))
        songlist = [song1, song2, song3, song4]
        self.assertEqual(hw2.song_shorter_than(songlist, song), [song1, song4])

    # Part 4
    def test_running_time1(self):
        song1 = data.Song("singer A", "Track A", data.Duration(3, 12))
        song2 = data.Song("singer B", "Track B", data.Duration(3, 52))
        song3 = data.Song("singer C", "Track C", data.Duration(3, 14))
        song4 = data.Song("singer D", "Track D", data.Duration(0, 20))
        lista = [song1, song2, song3, song4]
        listb = [0, 0, 1, -1, -1, 3, 2, 2, 4]
        self.assertEqual(hw2.running_time(lista, listb), data.Duration(17, 4))

    def test_running_time2(self):
        song1 = data.Song("singer A", "Track A", data.Duration(2, 42))
        song2 = data.Song("singer B", "Track B", data.Duration(3, 44))
        song3 = data.Song("singer C", "Track C", data.Duration(2, 18))
        song4 = data.Song("singer D", "Track D", data.Duration(2, 58))
        lista = [song1, song2, song3, song4]
        listb = [0, 1, 2, -1, -3, 5, 1, 3, 6]
        self.assertEqual(hw2.running_time(lista, listb), data.Duration(15, 26))

    # Part 5
    def test_validate_route1(self):
        links = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
        sampleroute = ["a", "b", "c", "d", "e", "d", "b"]
        self.assertEqual(hw2.validate_route(links, sampleroute), False)

    def test_validate_route2(self):
        links = [["a", "b"], ["b", "c"], ["c", "d"], ["d", "e"]]
        sampleroute = ["b"]
        self.assertEqual(hw2.validate_route(links, sampleroute), True)

    # Part 6
    def test_longest_repitition1(self):
        numberlist = [5, 1, 2, 2, 2, 6, 4, 4, 4, 4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(hw2.longest_repitition(numberlist), 12)

    def test_longest_repitition2(self):
        numberlist = [6, 7, 17, 80, 80, -40, -40, -40, 6, 6, 6, 11, 6, 13, 4]
        self.assertEqual(hw2.longest_repitition(numberlist), 5)




if __name__ == '__main__':
    unittest.main()
