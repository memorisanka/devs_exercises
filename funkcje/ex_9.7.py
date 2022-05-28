def what_degree(hour, minute):
    """Funkcja zwraca kąt pomiędzy wskazówkami zegara o podanej godzinie i minucie.
    Funkcja korzysta z tzw. równania zegara.
    Kąt jest dodatni, gdy duża wskazówka wyprzedza małą.
    Kąt jest ujemny gdy mała wskazówka wyprzedza dużą.
    Kąt jest wynosi 0 gdy wskazówki pokrywają się."""

    if hour > 12:
        hour -= 12
    alpha = (11/2) * minute - 30 * hour
    return abs(alpha)


print(what_degree(11, 45))
