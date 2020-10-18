def update_dict(d, d2):
     for k, v in d2.items():
         if not k in d:
            d[k] = v

addressbook = {'mickey':'555-112233', 
                'goofy':'555-214365', 
                'pluto':'555-654321'}

ab = {'goofy':'555-333333',
       'donald':'444-111111',
       'daisy':'444-222222'}

update_dict(addressbook, ab)

print addressbook