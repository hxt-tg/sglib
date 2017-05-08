from __init__ import SteamGameOnline

def main():
    game = SteamGameOnline(292030, 0)
    
    # Test print individually.
    print game.img
    print game.description
    print game.user_reviews
    print game.recent_user_review
    print game.overall_user_review
    print game.app_tag
    print game.developer
    print game.publisher
    print '========================\n'
    
    # Test gid changing and reloading
    game.gtag = 'app'
    game.gid = 358040
    
    # Test __str__ and __unicode__
    print unicode(game)
    print '========================\n'
    
    # Test documentation
    help(SteamGameOnline)
    
if __name__ == '__main__':
    main()
