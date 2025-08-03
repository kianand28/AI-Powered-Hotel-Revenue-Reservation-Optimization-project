def filter_data(df, hotel_type=None, room_type=None, customer_type=None):
    if hotel_type:
        df = df[df['hotel'] == hotel_type]
    if room_type:
        df = df[df['reserved_room_type'] == room_type]
    if customer_type:
        df = df[df['customer_type'] == customer_type]
    return df
