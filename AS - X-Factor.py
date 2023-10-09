import random

#In terms of rows:
#1 = Taylor Swift
#2 = Justin Bieber
#3 = Ed Sheeran
#4 = Queen
#5 = The Weeknd
#6 = The Beatles
#7 = Eminem
#8 = Drake
#9 = Adele
#10 = Michael Jackson

artists = ['Taylor Swift', 'Justin Bieber', 'Ed Sheeran', 'Queen', 'The Weeknd', 'The Beatles', 'Eminem', 'Drake', 'Adele', 'Michael Jackson']

songs = [['Blank Space', 'You Belong With Me', 'Bad Blood', 'Look What You Made Me Do', 'Love Story', 'Anti-Hero', 'Maroon', 'Lavender Haze', 'White Horse', 'Karma'], ['Sorry', 'I Don’t Care', 'What Do You Mean?', 'Love Yourself', 'Where Are U Now?', 'Stay', 'Cold Water', 'Let Me Love You', 'Stuck With U', 'Peaches'], ['Thinking Out Loud', 'Shape of You', 'Perfect', 'The A Team', 'Photograph', 'Bad Habits', 'Castle on the Hill', 'Lego House', 'Shivers', 'Beautiful People'], ['Bohemian Rhapsody', 'Fat Bottomed Girls', 'Don’t Stop Me Now', 'Somebody to Love', 'Who Wants to Live Forever', 'Crazy Little Thing Called Love', 'Under Pressure', 'The Show Must Go On', 'Killer Queen', 'I Want to Break Free'], ['Blinding Lights', 'Coming Down', 'King Of The Fall', 'Sacrifice', 'Starboy', 'The Birds Pt.1', 'The Birds Pt.2', 'Rolling Stone', 'The Morning', 'Save Your Tears'], ['Come Together', 'Let It Be', 'Hey Jude', 'Something', 'In My Life', 'Yesterday', 'Strawberry Fields Forever', 'I Want to Hold Your Hand', 'A Day in the Life', 'While My Guitar Gently Weeps'], ['Lose Yourself', 'Stan', 'The Real Slim Shady', 'Without Me', 'The Way I Am', 'My Name Is', 'Role Model', "Cleanin’ Out My Closet", 'White America', 'Kim'], ['Nice For What', 'Child’s Play', 'Hold On, We’re Going Home', 'Hotline Bling', 'Portland', 'Know Yourself', 'Laugh Now Cry Later', 'Started From the Bottom', 'Fancy ', 'The Ride'], ['Easy on Me', 'When We Were Young', 'Hello', 'Skyfall', 'Rumour Has It', 'Someone Like You', 'Set Fire To The Rain', 'Rolling in the Deep', 'Chasing Pavements', 'Hometown Glory'], ['Billie Jean', 'Thriller', 'Rock With You', 'Smooth Criminal', 'Don’t Stop ‘Til You Get Enough', 'P.Y.T. (Pretty Young Thing)', 'Black Or White', 'Bad', 'Off The Wall', 'Beat It']]

ban1 = 99
ban2 = 99
count = 0
while count < 20:
  RandomArtist = random.randint(0, 9)
  if RandomArtist != ban1 and RandomArtist != ban2:
    ban1 = ban2
    ban2 = RandomArtist
    RandomSong = random.randint(0, 9)
    print(songs[RandomArtist][RandomSong], 'by', artists[RandomArtist])
    print('')
    count = count + 1
