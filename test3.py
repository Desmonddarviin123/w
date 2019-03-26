Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from requests import get
>>> url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
>>> response = get(url)
>>> print(response.text[:500])


<!DOCTYPE html>
<html
    xmlns:og="http://ogp.me/ns#"
    xmlns:fb="http://www.facebook.com/2008/fbml">
    <head>
         
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///?src=mdot">



        <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script>

<script>
    if (typeof uet == 'function') {
      uet("bb", "LoadTitle",
>>> from bs4
SyntaxError: invalid syntax
>>> from bs4 import BeautifulSoup
>>> html_soup = BeautifulSoup(response.text, 'html.parser')
>>> type(html_soup )
<class 'bs4.BeautifulSoup'>
>>> movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
>>> print (type(movie_containers))
<class 'bs4.element.ResultSet'>
>>> print (len(movie_containers))
50
>>> find_all(50)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    find_all(50)
NameError: name 'find_all' is not defined
>>> find (50)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    find (50)
NameError: name 'find' is not defined
>>> movie_containers
[<div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3315342"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3315342/?ref_=adv_li_i"> <img alt="Logan" class="loadlate" data-tconst="tt3315342" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BYzc5MTU4N2EtYTkyMi00NjdhLTg3NWEtMTY4OTEyMzJhZTAzXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">1.</span>
<a href="/title/tt3315342/?ref_=adv_li_tt">Logan</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">137 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Drama, Sci-Fi            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.1" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.1</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3315342" id="urv_tt3315342">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3315342">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3315342|imdb|8.1|8.1|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.1/10 (543,821 votes) - click stars to rate">
<meta content="8.1" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="543821" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 113.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.1</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3315342/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">77        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In a future where mutants are nearly extinct, an elderly and weary Logan leads a quiet life. But when Laura, a mutant child pursued by scientists, comes to him for help, he must get her to safety.</p>
<p class="">
    Director:
<a href="/name/nm0003506/?ref_=adv_li_dr_0">James Mangold</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0413168/?ref_=adv_li_st_0">Hugh Jackman</a>, 
<a href="/name/nm0001772/?ref_=adv_li_st_1">Patrick Stewart</a>, 
<a href="/name/nm6748436/?ref_=adv_li_st_2">Dafne Keen</a>, 
<a href="/name/nm2933542/?ref_=adv_li_st_3">Boyd Holbrook</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="543821" name="nv">543,821</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="226,277,068" name="nv">$226.28M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt0451279"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt0451279/?ref_=adv_li_i"> <img alt="Wonder Woman" class="loadlate" data-tconst="tt0451279" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">2.</span>
<a href="/title/tt0451279/?ref_=adv_li_tt">Wonder Woman</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">141 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt0451279" id="urv_tt0451279">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt0451279">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt0451279|imdb|7.5|7.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.5/10 (473,336 votes) - click stars to rate">
<meta content="7.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="473336" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 105px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt0451279/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">76        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, leaves home to fight a war, discovering her full powers and true destiny.</p>
<p class="">
    Director:
<a href="/name/nm0420941/?ref_=adv_li_dr_0">Patty Jenkins</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2933757/?ref_=adv_li_st_0">Gal Gadot</a>, 
<a href="/name/nm1517976/?ref_=adv_li_st_1">Chris Pine</a>, 
<a href="/name/nm0000705/?ref_=adv_li_st_2">Robin Wright</a>, 
<a href="/name/nm0205063/?ref_=adv_li_st_3">Lucy Davis</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="473336" name="nv">473,336</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="412,563,408" name="nv">$412.56M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3896198"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3896198/?ref_=adv_li_i"> <img alt="Guardians of the Galaxy Vol. 2" class="loadlate" data-tconst="tt3896198" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">3.</span>
<a href="/title/tt3896198/?ref_=adv_li_tt">Guardians of the Galaxy Vol. 2</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">136 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.7</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3896198" id="urv_tt3896198">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3896198">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3896198|imdb|7.7|7.7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.7/10 (456,499 votes) - click stars to rate">
<meta content="7.7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="456499" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 107.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3896198/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">67        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.</p>
<p class="">
    Director:
<a href="/name/nm0348181/?ref_=adv_li_dr_0">James Gunn</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0695435/?ref_=adv_li_st_0">Chris Pratt</a>, 
<a href="/name/nm0757855/?ref_=adv_li_st_1">Zoe Saldana</a>, 
<a href="/name/nm1176985/?ref_=adv_li_st_2">Dave Bautista</a>, 
<a href="/name/nm0004874/?ref_=adv_li_st_3">Vin Diesel</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="456499" name="nv">456,499</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="389,813,101" name="nv">$389.81M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5013056"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5013056/?ref_=adv_li_i"> <img alt="Dunkirk" class="loadlate" data-tconst="tt5013056" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BN2YyZjQ0NTEtNzU5MS00NGZkLTg0MTEtYzJmMWY3MWRhZjM2XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">4.</span>
<a href="/title/tt5013056/?ref_=adv_li_tt">Dunkirk</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">106 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Drama, History            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.9" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.9</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5013056" id="urv_tt5013056">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5013056">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5013056|imdb|7.9|7.9|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.9/10 (454,854 votes) - click stars to rate">
<meta content="7.9" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="454854" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 110.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.9</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5013056/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">94        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Allied soldiers from Belgium, the British Empire, and France are surrounded by the German Army, and evacuated during a fierce battle in World War II.</p>
<p class="">
    Director:
<a href="/name/nm0634240/?ref_=adv_li_dr_0">Christopher Nolan</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm7887725/?ref_=adv_li_st_0">Fionn Whitehead</a>, 
<a href="/name/nm4422686/?ref_=adv_li_st_1">Barry Keoghan</a>, 
<a href="/name/nm0753314/?ref_=adv_li_st_2">Mark Rylance</a>, 
<a href="/name/nm0362766/?ref_=adv_li_st_3">Tom Hardy</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="454854" name="nv">454,854</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="188,373,161" name="nv">$188.37M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2527336"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2527336/?ref_=adv_li_i"> <img alt="Star Wars: Episode VIII - The Last Jedi" class="loadlate" data-tconst="tt2527336" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">5.</span>
<a href="/title/tt2527336/?ref_=adv_li_tt">Star Wars: Episode VIII - The Last Jedi</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">U</span>
<span class="ghost">|</span>
<span class="runtime">152 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.2" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.2</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2527336" id="urv_tt2527336">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2527336">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2527336|imdb|7.2|7.2|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.2/10 (450,736 votes) - click stars to rate">
<meta content="7.2" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="450736" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 100.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2527336/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">85        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.</p>
<p class="">
    Director:
<a href="/name/nm0426059/?ref_=adv_li_dr_0">Rian Johnson</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm5397459/?ref_=adv_li_st_0">Daisy Ridley</a>, 
<a href="/name/nm3915784/?ref_=adv_li_st_1">John Boyega</a>, 
<a href="/name/nm0000434/?ref_=adv_li_st_2">Mark Hamill</a>, 
<a href="/name/nm0000402/?ref_=adv_li_st_3">Carrie Fisher</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="450736" name="nv">450,736</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="620,181,382" name="nv">$620.18M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3501632"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3501632/?ref_=adv_li_i"> <img alt="Thor: Ragnarok" class="loadlate" data-tconst="tt3501632" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">6.</span>
<a href="/title/tt3501632/?ref_=adv_li_tt">Thor: Ragnarok</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">130 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.9" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.9</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3501632" id="urv_tt3501632">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3501632">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3501632|imdb|7.9|7.9|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.9/10 (446,727 votes) - click stars to rate">
<meta content="7.9" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="446727" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 110.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.9</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3501632/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">74        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.</p>
<p class="">
    Director:
<a href="/name/nm0169806/?ref_=adv_li_dr_0">Taika Waititi</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm1165110/?ref_=adv_li_st_0">Chris Hemsworth</a>, 
<a href="/name/nm1089991/?ref_=adv_li_st_1">Tom Hiddleston</a>, 
<a href="/name/nm0000949/?ref_=adv_li_st_2">Cate Blanchett</a>, 
<a href="/name/nm0749263/?ref_=adv_li_st_3">Mark Ruffalo</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="446727" name="nv">446,727</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="315,058,289" name="nv">$315.06M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2250912"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2250912/?ref_=adv_li_i"> <img alt="Spider-Man: Homecoming" class="loadlate" data-tconst="tt2250912" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">7.</span>
<a href="/title/tt2250912/?ref_=adv_li_tt">Spider-Man: Homecoming</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">133 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Sci-Fi            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2250912" id="urv_tt2250912">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2250912">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2250912|imdb|7.5|7.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.5/10 (401,125 votes) - click stars to rate">
<meta content="7.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="401125" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 105px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2250912/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">73        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.</p>
<p class="">
    Director:
<a href="/name/nm1218281/?ref_=adv_li_dr_0">Jon Watts</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm4043618/?ref_=adv_li_st_0">Tom Holland</a>, 
<a href="/name/nm0000474/?ref_=adv_li_st_1">Michael Keaton</a>, 
<a href="/name/nm0000375/?ref_=adv_li_st_2">Robert Downey Jr.</a>, 
<a href="/name/nm0000673/?ref_=adv_li_st_3">Marisa Tomei</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="401125" name="nv">401,125</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="334,201,140" name="nv">$334.20M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5052448"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5052448/?ref_=adv_li_i"> <img alt="Get Out" class="loadlate" data-tconst="tt5052448" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">8.</span>
<a href="/title/tt5052448/?ref_=adv_li_tt">Get Out</a>
<span class="lister-item-year text-muted unbold">(I) (2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">104 min</span>
<span class="ghost">|</span>
<span class="genre">
Horror, Mystery, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.7</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5052448" id="urv_tt5052448">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5052448">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5052448|imdb|7.7|7.7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.7/10 (379,982 votes) - click stars to rate">
<meta content="7.7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="379982" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 107.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5052448/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">84        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.</p>
<p class="">
    Director:
<a href="/name/nm1443502/?ref_=adv_li_dr_0">Jordan Peele</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2257207/?ref_=adv_li_st_0">Daniel Kaluuya</a>, 
<a href="/name/nm4129745/?ref_=adv_li_st_1">Allison Williams</a>, 
<a href="/name/nm0925966/?ref_=adv_li_st_2">Bradley Whitford</a>, 
<a href="/name/nm0001416/?ref_=adv_li_st_3">Catherine Keener</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="379982" name="nv">379,982</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="176,040,665" name="nv">$176.04M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1856101"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1856101/?ref_=adv_li_i"> <img alt="Blade Runner 2049" class="loadlate" data-tconst="tt1856101" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">9.</span>
<a href="/title/tt1856101/?ref_=adv_li_tt">Blade Runner 2049</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">164 min</span>
<span class="ghost">|</span>
<span class="genre">
Drama, Mystery, Sci-Fi            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.0</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1856101" id="urv_tt1856101">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1856101">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1856101|imdb|8|8|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8/10 (367,526 votes) - click stars to rate">
<meta content="8" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="367526" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 112px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1856101/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">81        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A young blade runner's discovery of a long-buried secret leads him to track down former blade runner Rick Deckard, who's been missing for thirty years.</p>
<p class="">
    Director:
<a href="/name/nm0898288/?ref_=adv_li_dr_0">Denis Villeneuve</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000148/?ref_=adv_li_st_0">Harrison Ford</a>, 
<a href="/name/nm0331516/?ref_=adv_li_st_1">Ryan Gosling</a>, 
<a href="/name/nm1869101/?ref_=adv_li_st_2">Ana de Armas</a>, 
<a href="/name/nm1176985/?ref_=adv_li_st_3">Dave Bautista</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="367526" name="nv">367,526</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="92,054,159" name="nv">$92.05M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3890160"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3890160/?ref_=adv_li_i"> <img alt="Baby Driver" class="loadlate" data-tconst="tt3890160" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">10.</span>
<a href="/title/tt3890160/?ref_=adv_li_tt">Baby Driver</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">112 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Crime, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3890160" id="urv_tt3890160">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3890160">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3890160|imdb|7.6|7.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.6/10 (351,662 votes) - click stars to rate">
<meta content="7.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="351662" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 106.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3890160/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">86        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    After being coerced into working for a crime boss, a young getaway driver finds himself taking part in a heist doomed to fail.</p>
<p class="">
    Director:
<a href="/name/nm0942367/?ref_=adv_li_dr_0">Edgar Wright</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm5052065/?ref_=adv_li_st_0">Ansel Elgort</a>, 
<a href="/name/nm1256532/?ref_=adv_li_st_1">Jon Bernthal</a>, 
<a href="/name/nm0358316/?ref_=adv_li_st_2">Jon Hamm</a>, 
<a href="/name/nm2555462/?ref_=adv_li_st_3">Eiza González</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="351662" name="nv">351,662</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="107,825,862" name="nv">$107.83M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1396484"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1396484/?ref_=adv_li_i"> <img alt="It" class="loadlate" data-tconst="tt1396484" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjYi00ZjhhLWE1ODEtMWMzMWMzNDA0NmQ4XkEyXkFqcGdeQXVyNzYzODM3Mzg@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">11.</span>
<a href="/title/tt1396484/?ref_=adv_li_tt">It</a>
<span class="lister-item-year text-muted unbold">(I) (2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">135 min</span>
<span class="ghost">|</span>
<span class="genre">
Horror, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1396484" id="urv_tt1396484">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1396484">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1396484|imdb|7.4|7.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.4/10 (343,856 votes) - click stars to rate">
<meta content="7.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="343856" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 103.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1396484/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">69        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.</p>
<p class="">
    Director:
<a href="/name/nm0615592/?ref_=adv_li_dr_0">Andy Muschietti</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0803889/?ref_=adv_li_st_0">Bill Skarsgård</a>, 
<a href="/name/nm5897057/?ref_=adv_li_st_1">Jaeden Martell</a>, 
<a href="/name/nm6016511/?ref_=adv_li_st_2">Finn Wolfhard</a>, 
<a href="/name/nm6096118/?ref_=adv_li_st_3">Sophia Lillis</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="343856" name="nv">343,856</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="327,481,748" name="nv">$327.48M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5027774"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5027774/?ref_=adv_li_i"> <img alt="Three Billboards Outside Ebbing, Missouri" class="loadlate" data-tconst="tt5027774" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjMxNzgwMDUyMl5BMl5BanBnXkFtZTgwMTQ0NTIyNDM@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">12.</span>
<a href="/title/tt5027774/?ref_=adv_li_tt">Three Billboards Outside Ebbing, Missouri</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">115 min</span>
<span class="ghost">|</span>
<span class="genre">
Crime, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.2" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.2</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5027774" id="urv_tt5027774">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5027774">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5027774|imdb|8.2|8.2|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.2/10 (330,686 votes) - click stars to rate">
<meta content="8.2" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="330686" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 114.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5027774/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">88        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A mother personally challenges the local authorities to solve her daughter's murder when they fail to catch the culprit.</p>
<p class="">
    Director:
<a href="/name/nm1732981/?ref_=adv_li_dr_0">Martin McDonagh</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000531/?ref_=adv_li_st_0">Frances McDormand</a>, 
<a href="/name/nm0000437/?ref_=adv_li_st_1">Woody Harrelson</a>, 
<a href="/name/nm0005377/?ref_=adv_li_st_2">Sam Rockwell</a>, 
<a href="/name/nm2655177/?ref_=adv_li_st_3">Caleb Landry Jones</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="330686" name="nv">330,686</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="54,513,740" name="nv">$54.51M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt0974015"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt0974015/?ref_=adv_li_i"> <img alt="Justice League" class="loadlate" data-tconst="tt0974015" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BYWVhZjZkYTItOGIwYS00NmRkLWJlYjctMWM0ZjFmMDU4ZjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">13.</span>
<a href="/title/tt0974015/?ref_=adv_li_tt">Justice League</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">120 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt0974015" id="urv_tt0974015">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt0974015">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt0974015|imdb|6.5|6.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.5/10 (318,759 votes) - click stars to rate">
<meta content="6.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="318759" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 91px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt0974015/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">45        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Fueled by his restored faith in humanity and inspired by Superman's selfless act, Bruce Wayne enlists the help of his new-found ally, Diana Prince, to face an even greater enemy.</p>
<p class="">
    Director:
<a href="/name/nm0811583/?ref_=adv_li_dr_0">Zack Snyder</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000255/?ref_=adv_li_st_0">Ben Affleck</a>, 
<a href="/name/nm2933757/?ref_=adv_li_st_1">Gal Gadot</a>, 
<a href="/name/nm0597388/?ref_=adv_li_st_2">Jason Momoa</a>, 
<a href="/name/nm3009232/?ref_=adv_li_st_3">Ezra Miller</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="318759" name="nv">318,759</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="229,024,295" name="nv">$229.02M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5580390"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5580390/?ref_=adv_li_i"> <img alt="The Shape of Water" class="loadlate" data-tconst="tt5580390" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNGNiNWQ5M2MtNGI0OC00MDA2LWI5NzEtMmZiYjVjMDEyOWYzXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">14.</span>
<a href="/title/tt5580390/?ref_=adv_li_tt">The Shape of Water</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">123 min</span>
<span class="ghost">|</span>
<span class="genre">
Adventure, Drama, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.3" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.3</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5580390" id="urv_tt5580390">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5580390">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5580390|imdb|7.3|7.3|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.3/10 (297,443 votes) - click stars to rate">
<meta content="7.3" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="297443" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 102.2px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.3</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5580390/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">87        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    At a top secret research facility in the 1960s, a lonely janitor forms a unique relationship with an amphibious creature that is being held in captivity.</p>
<p class="">
    Director:
<a href="/name/nm0868219/?ref_=adv_li_dr_0">Guillermo del Toro</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm1020089/?ref_=adv_li_st_0">Sally Hawkins</a>, 
<a href="/name/nm0818055/?ref_=adv_li_st_1">Octavia Spencer</a>, 
<a href="/name/nm0788335/?ref_=adv_li_st_2">Michael Shannon</a>, 
<a href="/name/nm0427964/?ref_=adv_li_st_3">Doug Jones</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="297443" name="nv">297,443</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="63,859,435" name="nv">$63.86M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4425200"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4425200/?ref_=adv_li_i"> <img alt="John Wick: Chapter 2" class="loadlate" data-tconst="tt4425200" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">15.</span>
<a href="/title/tt4425200/?ref_=adv_li_tt">John Wick: Chapter 2</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">122 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Crime, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4425200" id="urv_tt4425200">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4425200">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4425200|imdb|7.5|7.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.5/10 (265,472 votes) - click stars to rate">
<meta content="7.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="265472" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 105px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4425200/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">75        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life.</p>
<p class="">
    Director:
<a href="/name/nm0821432/?ref_=adv_li_dr_0">Chad Stahelski</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000206/?ref_=adv_li_st_0">Keanu Reeves</a>, 
<a href="/name/nm1249052/?ref_=adv_li_st_1">Riccardo Scamarcio</a>, 
<a href="/name/nm0574534/?ref_=adv_li_st_2">Ian McShane</a>, 
<a href="/name/nm3199307/?ref_=adv_li_st_3">Ruby Rose</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="265472" name="nv">265,472</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="92,029,184" name="nv">$92.03M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2380307"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2380307/?ref_=adv_li_i"> <img alt="Coco" class="loadlate" data-tconst="tt2380307" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY98_CR1,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">16.</span>
<a href="/title/tt2380307/?ref_=adv_li_tt">Coco</a>
<span class="lister-item-year text-muted unbold">(I) (2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">U</span>
<span class="ghost">|</span>
<span class="runtime">105 min</span>
<span class="ghost">|</span>
<span class="genre">
Animation, Adventure, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2380307" id="urv_tt2380307">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2380307">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2380307|imdb|8.4|8.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.4/10 (263,626 votes) - click stars to rate">
<meta content="8.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="263626" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 117.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2380307/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">81        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.</p>
<p class="">
    Directors:
<a href="/name/nm0881279/?ref_=adv_li_dr_0">Lee Unkrich</a>, 
<a href="/name/nm2937122/?ref_=adv_li_dr_1">Adrian Molina</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm5645519/?ref_=adv_li_st_0">Anthony Gonzalez</a>, 
<a href="/name/nm0305558/?ref_=adv_li_st_1">Gael García Bernal</a>, 
<a href="/name/nm0000973/?ref_=adv_li_st_2">Benjamin Bratt</a>, 
<a href="/name/nm0005513/?ref_=adv_li_st_3">Alanna Ubach</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="263626" name="nv">263,626</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="209,726,015" name="nv">$209.73M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2283362"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2283362/?ref_=adv_li_i"> <img alt="Jumanji: Welcome to the Jungle" class="loadlate" data-tconst="tt2283362" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BODQ0NDhjYWItYTMxZi00NTk2LWIzNDEtOWZiYWYxZjc2MTgxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">17.</span>
<a href="/title/tt2283362/?ref_=adv_li_tt">Jumanji: Welcome to the Jungle</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">119 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.0</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2283362" id="urv_tt2283362">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2283362">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2283362|imdb|7|7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7/10 (234,707 votes) - click stars to rate">
<meta content="7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="234707" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 98px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2283362/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">58        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Four teenagers are sucked into a magical video game, and the only way they can escape is to work together to finish the game.</p>
<p class="">
    Director:
<a href="/name/nm0440458/?ref_=adv_li_dr_0">Jake Kasdan</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0425005/?ref_=adv_li_st_0">Dwayne Johnson</a>, 
<a href="/name/nm2394794/?ref_=adv_li_st_1">Karen Gillan</a>, 
<a href="/name/nm0366389/?ref_=adv_li_st_2">Kevin Hart</a>, 
<a href="/name/nm0085312/?ref_=adv_li_st_3">Jack Black</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="234707" name="nv">234,707</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="404,515,480" name="nv">$404.52M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2771200"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2771200/?ref_=adv_li_i"> <img alt="Beauty and the Beast" class="loadlate" data-tconst="tt2771200" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTUwNjUxMTM4NV5BMl5BanBnXkFtZTgwODExMDQzMTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">18.</span>
<a href="/title/tt2771200/?ref_=adv_li_tt">Beauty and the Beast</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">129 min</span>
<span class="ghost">|</span>
<span class="genre">
Family, Fantasy, Musical            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.2" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.2</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2771200" id="urv_tt2771200">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2771200">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2771200|imdb|7.2|7.2|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.2/10 (232,056 votes) - click stars to rate">
<meta content="7.2" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="232056" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 100.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2771200/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">65        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A selfish prince is cursed to become a monster for the rest of his life, unless he learns to fall in love with a beautiful young woman he keeps prisoner.</p>
<p class="">
    Director:
<a href="/name/nm0174374/?ref_=adv_li_dr_0">Bill Condon</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0914612/?ref_=adv_li_st_0">Emma Watson</a>, 
<a href="/name/nm1405398/?ref_=adv_li_st_1">Dan Stevens</a>, 
<a href="/name/nm1812656/?ref_=adv_li_st_2">Luke Evans</a>, 
<a href="/name/nm1265802/?ref_=adv_li_st_3">Josh Gad</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="232056" name="nv">232,056</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="504,014,165" name="nv">$504.01M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3731562"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3731562/?ref_=adv_li_i"> <img alt="Kong: Skull Island" class="loadlate" data-tconst="tt3731562" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTUwMzI5ODEwNF5BMl5BanBnXkFtZTgwNjAzNjI2MDI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">19.</span>
<a href="/title/tt3731562/?ref_=adv_li_tt">Kong: Skull Island</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">118 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3731562" id="urv_tt3731562">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3731562">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3731562|imdb|6.6|6.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.6/10 (230,654 votes) - click stars to rate">
<meta content="6.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="230654" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 92.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3731562/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">62        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    After the Vietnam war, a team of scientists explore an uncharted island in the Pacific, venturing into the domain of the mighty Kong, and must fight to escape a primal Eden.</p>
<p class="">
    Director:
<a href="/name/nm3611349/?ref_=adv_li_dr_0">Jordan Vogt-Roberts</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm1089991/?ref_=adv_li_st_0">Tom Hiddleston</a>, 
<a href="/name/nm0000168/?ref_=adv_li_st_1">Samuel L. Jackson</a>, 
<a href="/name/nm0488953/?ref_=adv_li_st_2">Brie Larson</a>, 
<a href="/name/nm0000604/?ref_=adv_li_st_3">John C. Reilly</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="230654" name="nv">230,654</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="168,052,812" name="nv">$168.05M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4649466"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4649466/?ref_=adv_li_i"> <img alt="Kingsman: The Golden Circle" class="loadlate" data-tconst="tt4649466" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjQ3OTgzMzY4NF5BMl5BanBnXkFtZTgwOTc4OTQyMzI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">20.</span>
<a href="/title/tt4649466/?ref_=adv_li_tt">Kingsman: The Golden Circle</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">141 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.8" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.8</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4649466" id="urv_tt4649466">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4649466">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4649466|imdb|6.8|6.8|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.8/10 (223,706 votes) - click stars to rate">
<meta content="6.8" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="223706" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 95.2px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4649466/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">44        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    When their headquarters are destroyed and the world is held hostage, the Kingsman's journey leads them to the discovery of an allied spy organization in the United States. These two elite secret organizations must band together to defeat a common enemy.</p>
<p class="">
    Director:
<a href="/name/nm0891216/?ref_=adv_li_dr_0">Matthew Vaughn</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm5473782/?ref_=adv_li_st_0">Taron Egerton</a>, 
<a href="/name/nm0000147/?ref_=adv_li_st_1">Colin Firth</a>, 
<a href="/name/nm0835016/?ref_=adv_li_st_2">Mark Strong</a>, 
<a href="/name/nm1475594/?ref_=adv_li_st_3">Channing Tatum</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="223706" name="nv">223,706</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="100,234,838" name="nv">$100.23M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1790809"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1790809/?ref_=adv_li_i"> <img alt="Pirates of the Caribbean: Dead Men Tell No Tales" class="loadlate" data-tconst="tt1790809" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTYyMTcxNzc5M15BMl5BanBnXkFtZTgwOTg2ODE2MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">21.</span>
<a href="/title/tt1790809/?ref_=adv_li_tt">Pirates of the Caribbean: Dead Men Tell No Tales</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">129 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1790809" id="urv_tt1790809">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1790809">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1790809|imdb|6.6|6.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.6/10 (222,652 votes) - click stars to rate">
<meta content="6.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="222652" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 92.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1790809/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore unfavorable">39        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Captain Jack Sparrow searches for the trident of Poseidon while being pursued by an undead sea captain and his crew.</p>
<p class="">
    Directors:
<a href="/name/nm1461392/?ref_=adv_li_dr_0">Joachim Rønning</a>, 
<a href="/name/nm1650283/?ref_=adv_li_dr_1">Espen Sandberg</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000136/?ref_=adv_li_st_0">Johnny Depp</a>, 
<a href="/name/nm0001691/?ref_=adv_li_st_1">Geoffrey Rush</a>, 
<a href="/name/nm0000849/?ref_=adv_li_st_2">Javier Bardem</a>, 
<a href="/name/nm0089217/?ref_=adv_li_st_3">Orlando Bloom</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="222652" name="nv">222,652</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="172,558,876" name="nv">$172.56M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2316204"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2316204/?ref_=adv_li_i"> <img alt="Alien: Covenant" class="loadlate" data-tconst="tt2316204" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BYzVkMjRhNzctOGQxMC00OGE2LWJhN2EtNmYyODRiMDNlM2ZmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">22.</span>
<a href="/title/tt2316204/?ref_=adv_li_tt">Alien: Covenant</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">122 min</span>
<span class="ghost">|</span>
<span class="genre">
Horror, Sci-Fi, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2316204" id="urv_tt2316204">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2316204">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2316204|imdb|6.4|6.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.4/10 (222,135 votes) - click stars to rate">
<meta content="6.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="222135" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 89.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2316204/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">65        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    The crew of a colony ship, bound for a remote planet, discover an uncharted paradise with a threat beyond their imagination, and must attempt a harrowing escape.</p>
<p class="">
    Director:
<a href="/name/nm0000631/?ref_=adv_li_dr_0">Ridley Scott</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm1055413/?ref_=adv_li_st_0">Michael Fassbender</a>, 
<a href="/name/nm2239702/?ref_=adv_li_st_1">Katherine Waterston</a>, 
<a href="/name/nm0001082/?ref_=adv_li_st_2">Billy Crudup</a>, 
<a href="/name/nm1144419/?ref_=adv_li_st_3">Danny McBride</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="222135" name="nv">222,135</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="74,262,031" name="nv">$74.26M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1837492"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1837492/?ref_=adv_li_i"> <img alt="13 Reasons Why" class="loadlate" data-tconst="tt1837492" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNDgwNDU2MjgwMl5BMl5BanBnXkFtZTgwMTE2NzQ0NTM@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">23.</span>
<a href="/title/tt1837492/?ref_=adv_li_tt">13 Reasons Why</a>
<span class="lister-item-year text-muted unbold">(2017– )</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">60 min</span>
<span class="ghost">|</span>
<span class="genre">
Drama, Mystery            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.0</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1837492" id="urv_tt1837492">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1837492">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1837492|imdb|8|8|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8/10 (205,243 votes) - click stars to rate">
<meta content="8" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="205243" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 112px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1837492/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
</div>
<p class="text-muted">
    Follows teenager Clay Jensen, in his quest to uncover the story behind his classmate and crush, Hannah, and her decision to end her life.</p>
<p class="">
            
    Stars:
<a href="/name/nm1910255/?ref_=adv_li_st_0">Dylan Minnette</a>, 
<a href="/name/nm7692698/?ref_=adv_li_st_1">Katherine Langford</a>, 
<a href="/name/nm2111303/?ref_=adv_li_st_2">Christian Navarro</a>, 
<a href="/name/nm2647981/?ref_=adv_li_st_3">Alisha Boe</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="205243" name="nv">205,243</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3450958"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3450958/?ref_=adv_li_i"> <img alt="War for the Planet of the Apes" class="loadlate" data-tconst="tt3450958" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNDNmYTQzMDEtMmY0MS00OTNjLTk4MjItMDZhMzkzOGI3MzA0XkEyXkFqcGdeQXVyNjk5NDA3OTk@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">24.</span>
<a href="/title/tt3450958/?ref_=adv_li_tt">War for the Planet of the Apes</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">140 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3450958" id="urv_tt3450958">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3450958">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3450958|imdb|7.5|7.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.5/10 (197,167 votes) - click stars to rate">
<meta content="7.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="197167" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 105px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3450958/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">82        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    After the apes suffer unimaginable losses, Caesar wrestles with his darker instincts and begins his own mythic quest to avenge his kind.</p>
<p class="">
    Director:
<a href="/name/nm0716257/?ref_=adv_li_dr_0">Matt Reeves</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0785227/?ref_=adv_li_st_0">Andy Serkis</a>, 
<a href="/name/nm0000437/?ref_=adv_li_st_1">Woody Harrelson</a>, 
<a href="/name/nm0001872/?ref_=adv_li_st_2">Steve Zahn</a>, 
<a href="/name/nm0465269/?ref_=adv_li_st_3">Karin Konoval</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="197167" name="nv">197,167</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="146,880,162" name="nv">$146.88M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1485796"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1485796/?ref_=adv_li_i"> <img alt="The Greatest Showman" class="loadlate" data-tconst="tt1485796" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjI1NDYzNzY2Ml5BMl5BanBnXkFtZTgwODQwODczNTM@._V1_UY98_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">25.</span>
<a href="/title/tt1485796/?ref_=adv_li_tt">The Greatest Showman</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">105 min</span>
<span class="ghost">|</span>
<span class="genre">
Biography, Drama, Musical            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1485796" id="urv_tt1485796">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1485796">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1485796|imdb|7.6|7.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.6/10 (193,356 votes) - click stars to rate">
<meta content="7.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="193356" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 106.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1485796/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">48        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.</p>
<p class="">
    Director:
<a href="/name/nm1243905/?ref_=adv_li_dr_0">Michael Gracey</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0413168/?ref_=adv_li_st_0">Hugh Jackman</a>, 
<a href="/name/nm0931329/?ref_=adv_li_st_1">Michelle Williams</a>, 
<a href="/name/nm1374980/?ref_=adv_li_st_2">Zac Efron</a>, 
<a href="/name/nm3918035/?ref_=adv_li_st_3">Zendaya</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="193356" name="nv">193,356</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="174,340,174" name="nv">$174.34M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5442430"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5442430/?ref_=adv_li_i"> <img alt="Life" class="loadlate" data-tconst="tt5442430" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMzAwMmQxNTctYjVmYi00MDdlLWEzMWUtOTE5NTRiNDhhNjI2L2ltYWdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">26.</span>
<a href="/title/tt5442430/?ref_=adv_li_tt">Life</a>
<span class="lister-item-year text-muted unbold">(I) (2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">104 min</span>
<span class="ghost">|</span>
<span class="genre">
Horror, Sci-Fi, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5442430" id="urv_tt5442430">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5442430">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5442430|imdb|6.6|6.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.6/10 (178,713 votes) - click stars to rate">
<meta content="6.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="178713" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 92.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5442430/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">54        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A team of scientists aboard the International Space Station discover a rapidly evolving life form that caused extinction on Mars and now threatens all life on Earth.</p>
<p class="">
    Director:
<a href="/name/nm1174251/?ref_=adv_li_dr_0">Daniel Espinosa</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0350453/?ref_=adv_li_st_0">Jake Gyllenhaal</a>, 
<a href="/name/nm0272581/?ref_=adv_li_st_1">Rebecca Ferguson</a>, 
<a href="/name/nm0005351/?ref_=adv_li_st_2">Ryan Reynolds</a>, 
<a href="/name/nm0760796/?ref_=adv_li_st_3">Hiroyuki Sanada</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="178713" name="nv">178,713</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="30,234,022" name="nv">$30.23M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4630562"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4630562/?ref_=adv_li_i"> <img alt="The Fate of the Furious" class="loadlate" data-tconst="tt4630562" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">27.</span>
<a href="/title/tt4630562/?ref_=adv_li_tt">The Fate of the Furious</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">136 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Crime, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.7</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4630562" id="urv_tt4630562">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4630562">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4630562|imdb|6.7|6.7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.7/10 (176,061 votes) - click stars to rate">
<meta content="6.7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="176061" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 93.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4630562/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">56        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    When a mysterious woman seduces Dom into the world of terrorism and a betrayal of those closest to him, the crew face trials that will test them as never before.</p>
<p class="">
    Director:
<a href="/name/nm0336620/?ref_=adv_li_dr_0">F. Gary Gray</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0004874/?ref_=adv_li_st_0">Vin Diesel</a>, 
<a href="/name/nm0005458/?ref_=adv_li_st_1">Jason Statham</a>, 
<a href="/name/nm0425005/?ref_=adv_li_st_2">Dwayne Johnson</a>, 
<a href="/name/nm0735442/?ref_=adv_li_st_3">Michelle Rodriguez</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="176061" name="nv">176,061</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="226,008,385" name="nv">$226.01M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3402236"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3402236/?ref_=adv_li_i"> <img alt="Murder on the Orient Express" class="loadlate" data-tconst="tt3402236" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTAxNDkxODIyMDZeQTJeQWpwZ15BbWU4MDQ2Mjg4NDIy._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">28.</span>
<a href="/title/tt3402236/?ref_=adv_li_tt">Murder on the Orient Express</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">114 min</span>
<span class="ghost">|</span>
<span class="genre">
Crime, Drama, Mystery            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3402236" id="urv_tt3402236">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3402236">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3402236|imdb|6.5|6.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.5/10 (174,521 votes) - click stars to rate">
<meta content="6.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="174521" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 91px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3402236/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">52        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    When a murder occurs on the train on which he's travelling, celebrated detective Hercule Poirot is recruited to solve the case.</p>
<p class="">
    Director:
<a href="/name/nm0000110/?ref_=adv_li_dr_0">Kenneth Branagh</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000110/?ref_=adv_li_st_0">Kenneth Branagh</a>, 
<a href="/name/nm0004851/?ref_=adv_li_st_1">Penélope Cruz</a>, 
<a href="/name/nm0000353/?ref_=adv_li_st_2">Willem Dafoe</a>, 
<a href="/name/nm0001132/?ref_=adv_li_st_3">Judi Dench</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="174521" name="nv">174,521</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="102,826,543" name="nv">$102.83M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1219827"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1219827/?ref_=adv_li_i"> <img alt="Ghost in the Shell" class="loadlate" data-tconst="tt1219827" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMzJiNTI3MjItMGJiMy00YzA1LTg2MTItZmE1ZmRhOWQ0NGY1XkEyXkFqcGdeQXVyOTk4MTM0NQ@@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">29.</span>
<a href="/title/tt1219827/?ref_=adv_li_tt">Ghost in the Shell</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">107 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Drama, Sci-Fi            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1219827" id="urv_tt1219827">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1219827">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1219827|imdb|6.4|6.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.4/10 (172,631 votes) - click stars to rate">
<meta content="6.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="172631" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 89.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1219827/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">52        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In the near future, Major Mira Killian is the first of her kind: A human saved from a terrible crash, who is cyber-enhanced to be a perfect soldier devoted to stopping the world's most dangerous criminals.</p>
<p class="">
    Director:
<a href="/name/nm2782185/?ref_=adv_li_dr_0">Rupert Sanders</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0424060/?ref_=adv_li_st_0">Scarlett Johansson</a>, 
<a href="/name/nm1561982/?ref_=adv_li_st_1">Pilou Asbæk</a>, 
<a href="/name/nm0001429/?ref_=adv_li_st_2">Takeshi Kitano</a>, 
<a href="/name/nm0000300/?ref_=adv_li_st_3">Juliette Binoche</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="172631" name="nv">172,631</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="40,533,014" name="nv">$40.53M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4925292"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4925292/?ref_=adv_li_i"> <img alt="Lady Bird" class="loadlate" data-tconst="tt4925292" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BODhkZGE0NDQtZDc0Zi00YmQ4LWJiNmUtYTY1OGM1ODRmNGVkXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">30.</span>
<a href="/title/tt4925292/?ref_=adv_li_tt">Lady Bird</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">94 min</span>
<span class="ghost">|</span>
<span class="genre">
Comedy, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4925292" id="urv_tt4925292">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4925292">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4925292|imdb|7.4|7.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.4/10 (171,469 votes) - click stars to rate">
<meta content="7.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="171469" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 103.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4925292/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">94        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In 2002, an artistically inclined seventeen-year-old girl comes of age in Sacramento, California.</p>
<p class="">
    Director:
<a href="/name/nm1950086/?ref_=adv_li_dr_0">Greta Gerwig</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm1519680/?ref_=adv_li_st_0">Saoirse Ronan</a>, 
<a href="/name/nm0582418/?ref_=adv_li_st_1">Laurie Metcalf</a>, 
<a href="/name/nm0504832/?ref_=adv_li_st_2">Tracy Letts</a>, 
<a href="/name/nm2348627/?ref_=adv_li_st_3">Lucas Hedges</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="171469" name="nv">171,469</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="48,958,273" name="nv">$48.96M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1972591"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1972591/?ref_=adv_li_i"> <img alt="King Arthur: Legend of the Sword" class="loadlate" data-tconst="tt1972591" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjM3ODY3Njc5Ml5BMl5BanBnXkFtZTgwMjQ5NjM5MTI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">31.</span>
<a href="/title/tt1972591/?ref_=adv_li_tt">King Arthur: Legend of the Sword</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">126 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.8" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.8</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1972591" id="urv_tt1972591">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1972591">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1972591|imdb|6.8|6.8|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.8/10 (165,016 votes) - click stars to rate">
<meta content="6.8" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="165016" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 95.2px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.8</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1972591/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">41        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Robbed of his birthright, Arthur comes up the hard way in the back alleys of the city. But once he pulls the sword from the stone, he is forced to acknowledge his true legacy - whether he likes it or not.</p>
<p class="">
    Director:
<a href="/name/nm0005363/?ref_=adv_li_dr_0">Guy Ritchie</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0402271/?ref_=adv_li_st_0">Charlie Hunnam</a>, 
<a href="/name/nm2793591/?ref_=adv_li_st_1">Astrid Bergès-Frisbey</a>, 
<a href="/name/nm0000179/?ref_=adv_li_st_2">Jude Law</a>, 
<a href="/name/nm0005023/?ref_=adv_li_st_3">Djimon Hounsou</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="165016" name="nv">165,016</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="39,175,066" name="nv">$39.18M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5362988"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5362988/?ref_=adv_li_i"> <img alt="Wind River" class="loadlate" data-tconst="tt5362988" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTUyMjU1OTUwM15BMl5BanBnXkFtZTgwMDg1NDQ2MjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">32.</span>
<a href="/title/tt5362988/?ref_=adv_li_tt">Wind River</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">R</span>
<span class="ghost">|</span>
<span class="runtime">107 min</span>
<span class="ghost">|</span>
<span class="genre">
Crime, Drama, Mystery            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.7</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5362988" id="urv_tt5362988">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5362988">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5362988|imdb|7.7|7.7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.7/10 (163,992 votes) - click stars to rate">
<meta content="7.7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="163992" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 107.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5362988/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">73        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A veteran hunter helps an FBI agent investigate the murder of a young woman on a Wyoming Native American reservation.</p>
<p class="">
    Director:
<a href="/name/nm0792263/?ref_=adv_li_dr_0">Taylor Sheridan</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2080328/?ref_=adv_li_st_0">Kelsey Asbille</a>, 
<a href="/name/nm0719637/?ref_=adv_li_st_1">Jeremy Renner</a>, 
<a href="/name/nm1247407/?ref_=adv_li_st_2">Julia Jones</a>, 
<a href="/name/nm3897067/?ref_=adv_li_st_3">Teo Briones</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="163992" name="nv">163,992</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="33,800,859" name="nv">$33.80M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1959563"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1959563/?ref_=adv_li_i"> <img alt="The Hitman's Bodyguard" class="loadlate" data-tconst="tt1959563" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjQ5NjA2NDg1MV5BMl5BanBnXkFtZTgwMDAzNDc4MjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">33.</span>
<a href="/title/tt1959563/?ref_=adv_li_tt">The Hitman's Bodyguard</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">118 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Comedy, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.9" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.9</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1959563" id="urv_tt1959563">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1959563">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1959563|imdb|6.9|6.9|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.9/10 (157,765 votes) - click stars to rate">
<meta content="6.9" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="157765" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 96.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.9</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1959563/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">47        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    The world's top bodyguard gets a new client, a hitman who must testify at the International Criminal Court. They must put their differences aside and work together to make it to the trial on time.</p>
<p class="">
    Director:
<a href="/name/nm0400850/?ref_=adv_li_dr_0">Patrick Hughes</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0005351/?ref_=adv_li_st_0">Ryan Reynolds</a>, 
<a href="/name/nm0000168/?ref_=adv_li_st_1">Samuel L. Jackson</a>, 
<a href="/name/nm0000198/?ref_=adv_li_st_2">Gary Oldman</a>, 
<a href="/name/nm1392388/?ref_=adv_li_st_3">Elodie Yung</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="157765" name="nv">157,765</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="75,468,583" name="nv">$75.47M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5109784"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5109784/?ref_=adv_li_i"> <img alt="Mother!" class="loadlate" data-tconst="tt5109784" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMzc5ODExODE0MV5BMl5BanBnXkFtZTgwNDkzNDUxMzI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">34.</span>
<a href="/title/tt5109784/?ref_=adv_li_tt">Mother!</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">(Banned)</span>
<span class="ghost">|</span>
<span class="runtime">121 min</span>
<span class="ghost">|</span>
<span class="genre">
Drama, Horror, Mystery            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5109784" id="urv_tt5109784">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5109784">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5109784|imdb|6.6|6.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.6/10 (151,409 votes) - click stars to rate">
<meta content="6.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="151409" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 92.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5109784/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">75        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A couple's relationship is tested when uninvited guests arrive at their home, disrupting their tranquil existence.</p>
<p class="">
    Director:
<a href="/name/nm0004716/?ref_=adv_li_dr_0">Darren Aronofsky</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2225369/?ref_=adv_li_st_0">Jennifer Lawrence</a>, 
<a href="/name/nm0000849/?ref_=adv_li_st_1">Javier Bardem</a>, 
<a href="/name/nm0000438/?ref_=adv_li_st_2">Ed Harris</a>, 
<a href="/name/nm0000201/?ref_=adv_li_st_3">Michelle Pfeiffer</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="151409" name="nv">151,409</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="17,800,004" name="nv">$17.80M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2345759"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2345759/?ref_=adv_li_i"> <img alt="The Mummy" class="loadlate" data-tconst="tt2345759" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTkwMTgwODAxMl5BMl5BanBnXkFtZTgwNTEwNTQ3MDI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">35.</span>
<a href="/title/tt2345759/?ref_=adv_li_tt">The Mummy</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">110 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="5.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>5.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2345759" id="urv_tt2345759">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2345759">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2345759|imdb|5.5|5.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 5.5/10 (150,127 votes) - click stars to rate">
<meta content="5.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="150127" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 77px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">5.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2345759/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore unfavorable">34        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    An ancient Egyptian princess is awakened from her crypt beneath the desert, bringing with her malevolence grown over millennia, and terrors that defy human comprehension.</p>
<p class="">
    Director:
<a href="/name/nm0476064/?ref_=adv_li_dr_0">Alex Kurtzman</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000129/?ref_=adv_li_st_0">Tom Cruise</a>, 
<a href="/name/nm1154749/?ref_=adv_li_st_1">Sofia Boutella</a>, 
<a href="/name/nm1834115/?ref_=adv_li_st_2">Annabelle Wallis</a>, 
<a href="/name/nm0000128/?ref_=adv_li_st_3">Russell Crowe</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="150127" name="nv">150,127</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="80,101,125" name="nv">$80.10M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5726616"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5726616/?ref_=adv_li_i"> <img alt="Call Me by Your Name" class="loadlate" data-tconst="tt5726616" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNDk3NTEwNjc0MV5BMl5BanBnXkFtZTgwNzYxNTMwMzI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">36.</span>
<a href="/title/tt5726616/?ref_=adv_li_tt">Call Me by Your Name</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">132 min</span>
<span class="ghost">|</span>
<span class="genre">
Drama, Romance            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.9" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.9</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5726616" id="urv_tt5726616">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5726616">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5726616|imdb|7.9|7.9|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.9/10 (147,967 votes) - click stars to rate">
<meta content="7.9" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="147967" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 110.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.9</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5726616/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">93        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In 1980s Italy, a romance blossoms between a seventeen year-old student and the older man hired as his father's research assistant.</p>
<p class="">
    Director:
<a href="/name/nm0345174/?ref_=adv_li_dr_0">Luca Guadagnino</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2309517/?ref_=adv_li_st_0">Armie Hammer</a>, 
<a href="/name/nm3154303/?ref_=adv_li_st_1">Timothée Chalamet</a>, 
<a href="/name/nm0836121/?ref_=adv_li_st_2">Michael Stuhlbarg</a>, 
<a href="/name/nm0142972/?ref_=adv_li_st_3">Amira Casar</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="147967" name="nv">147,967</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="18,095,701" name="nv">$18.10M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2406566"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2406566/?ref_=adv_li_i"> <img alt="Atomic Blonde" class="loadlate" data-tconst="tt2406566" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjM5NDYzMzg5N15BMl5BanBnXkFtZTgwOTM2NDU1MjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">37.</span>
<a href="/title/tt2406566/?ref_=adv_li_tt">Atomic Blonde</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">115 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Mystery, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.7" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.7</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2406566" id="urv_tt2406566">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2406566">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2406566|imdb|6.7|6.7|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.7/10 (146,182 votes) - click stars to rate">
<meta content="6.7" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="146182" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 93.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.7</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2406566/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">63        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    An undercover MI6 agent is sent to Berlin during the Cold War to investigate the murder of a fellow agent and recover a missing list of double agents.</p>
<p class="">
    Director:
<a href="/name/nm0500610/?ref_=adv_li_dr_0">David Leitch</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000234/?ref_=adv_li_st_0">Charlize Theron</a>, 
<a href="/name/nm0564215/?ref_=adv_li_st_1">James McAvoy</a>, 
<a href="/name/nm0000422/?ref_=adv_li_st_2">John Goodman</a>, 
<a href="/name/nm0550371/?ref_=adv_li_st_3">Eddie Marsan</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="146182" name="nv">146,182</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="51,573,925" name="nv">$51.57M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5519340"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5519340/?ref_=adv_li_i"> <img alt="Bright" class="loadlate" data-tconst="tt5519340" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTcyNzk5NDg1Nl5BMl5BanBnXkFtZTgwNTM5MDQxNDM@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">38.</span>
<a href="/title/tt5519340/?ref_=adv_li_tt">Bright</a>
<span class="lister-item-year text-muted unbold">(I) (2017)</span>
</h3>
<p class="text-muted">
<span class="runtime">117 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Crime, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5519340" id="urv_tt5519340">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5519340">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5519340|imdb|6.4|6.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.4/10 (145,058 votes) - click stars to rate">
<meta content="6.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="145058" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 89.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5519340/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore unfavorable">29        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A detective must work with an Orc to find a powerful wand before evil creatures do.</p>
<p class="">
    Director:
<a href="/name/nm0043742/?ref_=adv_li_dr_0">David Ayer</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000226/?ref_=adv_li_st_0">Will Smith</a>, 
<a href="/name/nm0249291/?ref_=adv_li_st_1">Joel Edgerton</a>, 
<a href="/name/nm0636426/?ref_=adv_li_st_2">Noomi Rapace</a>, 
<a href="/name/nm1183149/?ref_=adv_li_st_3">Edgar Ramírez</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="145058" name="nv">145,058</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5675620"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5675620/?ref_=adv_li_i"> <img alt="The Punisher" class="loadlate" data-tconst="tt5675620" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTExODIwOTUxNzFeQTJeQWpwZ15BbWU4MDE5MDA0MTcz._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">39.</span>
<a href="/title/tt5675620/?ref_=adv_li_tt">The Punisher</a>
<span class="lister-item-year text-muted unbold">(2017–2019)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">53 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Crime            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5675620" id="urv_tt5675620">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5675620">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5675620|imdb|8.6|8.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.6/10 (142,216 votes) - click stars to rate">
<meta content="8.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="142216" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 120.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5675620/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
</div>
<p class="text-muted">
    After the murder of his family, Marine veteran Frank Castle becomes the vigilante known as "The Punisher," with only one goal in mind: to avenge them.</p>
<p class="">
            
    Stars:
<a href="/name/nm1256532/?ref_=adv_li_st_0">Jon Bernthal</a>, 
<a href="/name/nm2362244/?ref_=adv_li_st_1">Amber Rose Revah</a>, 
<a href="/name/nm1602660/?ref_=adv_li_st_2">Ben Barnes</a>, 
<a href="/name/nm2773505/?ref_=adv_li_st_3">Jason R. Moore</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="142216" name="nv">142,216</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt2239822"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt2239822/?ref_=adv_li_i"> <img alt="Valerian and the City of a Thousand Planets" class="loadlate" data-tconst="tt2239822" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTkxMDAxNDUyNV5BMl5BanBnXkFtZTgwOTc3MzcxMjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">40.</span>
<a href="/title/tt2239822/?ref_=adv_li_tt">Valerian and the City of a Thousand Planets</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">137 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Fantasy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="6.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>6.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt2239822" id="urv_tt2239822">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt2239822">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt2239822|imdb|6.5|6.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 6.5/10 (136,598 votes) - click stars to rate">
<meta content="6.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="136598" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 91px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">6.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt2239822/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore mixed">51        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A dark force threatens Alpha, a vast metropolis and home to species from a thousand planets. Special operatives Valerian and Laureline must race to identify the marauding menace and safeguard not just Alpha, but the future of the universe.</p>
<p class="">
    Director:
<a href="/name/nm0000108/?ref_=adv_li_dr_0">Luc Besson</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm2851530/?ref_=adv_li_st_0">Dane DeHaan</a>, 
<a href="/name/nm5353321/?ref_=adv_li_st_1">Cara Delevingne</a>, 
<a href="/name/nm0654110/?ref_=adv_li_st_2">Clive Owen</a>, 
<a href="/name/nm1982597/?ref_=adv_li_st_3">Rihanna</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="136598" name="nv">136,598</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="41,189,488" name="nv">$41.19M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5580036"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5580036/?ref_=adv_li_i"> <img alt="I, Tonya" class="loadlate" data-tconst="tt5580036" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMjI5MDY1NjYzMl5BMl5BanBnXkFtZTgwNjIzNDAxNDM@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">41.</span>
<a href="/title/tt5580036/?ref_=adv_li_tt">I, Tonya</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">120 min</span>
<span class="ghost">|</span>
<span class="genre">
Biography, Comedy, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5580036" id="urv_tt5580036">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5580036">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5580036|imdb|7.5|7.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.5/10 (136,168 votes) - click stars to rate">
<meta content="7.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="136168" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 105px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5580036/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">77        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Competitive ice skater <a href="/name/nm0002125">Tonya Harding</a> rises amongst the ranks at the U.S. Figure Skating Championships, but her future in the activity is thrown into doubt when her ex-husband intervenes.</p>
<p class="">
    Director:
<a href="/name/nm0318916/?ref_=adv_li_dr_0">Craig Gillespie</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm3053338/?ref_=adv_li_st_0">Margot Robbie</a>, 
<a href="/name/nm1659221/?ref_=adv_li_st_1">Sebastian Stan</a>, 
<a href="/name/nm0005049/?ref_=adv_li_st_2">Allison Janney</a>, 
<a href="/name/nm0629855/?ref_=adv_li_st_3">Julianne Nicholson</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="136168" name="nv">136,168</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="30,014,539" name="nv">$30.01M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4555426"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4555426/?ref_=adv_li_i"> <img alt="Darkest Hour" class="loadlate" data-tconst="tt4555426" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNTU4MjMwOTgyMV5BMl5BanBnXkFtZTgwODQzNjY2NDM@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">42.</span>
<a href="/title/tt4555426/?ref_=adv_li_tt">Darkest Hour</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">125 min</span>
<span class="ghost">|</span>
<span class="genre">
Biography, Drama, History            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4555426" id="urv_tt4555426">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4555426">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4555426|imdb|7.4|7.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.4/10 (132,591 votes) - click stars to rate">
<meta content="7.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="132591" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 103.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4555426/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">75        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    In May 1940, the fate of Western Europe hangs on British Prime Minister <a href="/name/nm0161476">Winston Churchill</a>, who must decide whether to negotiate with <a href="/name/nm0386944">Adolf Hitler</a>, or fight on knowing that it could mean a humiliating defeat for Britain and its empire.</p>
<p class="">
    Director:
<a href="/name/nm0942504/?ref_=adv_li_dr_0">Joe Wright</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000198/?ref_=adv_li_st_0">Gary Oldman</a>, 
<a href="/name/nm4141252/?ref_=adv_li_st_1">Lily James</a>, 
<a href="/name/nm0000218/?ref_=adv_li_st_2">Kristin Scott Thomas</a>, 
<a href="/name/nm0578853/?ref_=adv_li_st_3">Ben Mendelsohn</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="132591" name="nv">132,591</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="56,443,120" name="nv">$56.44M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt1469304"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt1469304/?ref_=adv_li_i"> <img alt="Baywatch" class="loadlate" data-tconst="tt1469304" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BNTA4MjQ0ODQzNF5BMl5BanBnXkFtZTgwNzA5NjYzMjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">43.</span>
<a href="/title/tt1469304/?ref_=adv_li_tt">Baywatch</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">116 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Comedy, Crime            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="5.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>5.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt1469304" id="urv_tt1469304">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt1469304">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt1469304|imdb|5.6|5.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 5.6/10 (131,063 votes) - click stars to rate">
<meta content="5.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="131063" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 78.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">5.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt1469304/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore unfavorable">37        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    Devoted lifeguard Mitch Buchannon butts heads with a brash new recruit, as they uncover a criminal plot that threatens the future of the bay.</p>
<p class="">
    Director:
<a href="/name/nm1164861/?ref_=adv_li_dr_0">Seth Gordon</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0425005/?ref_=adv_li_st_0">Dwayne Johnson</a>, 
<a href="/name/nm1374980/?ref_=adv_li_st_1">Zac Efron</a>, 
<a href="/name/nm1275259/?ref_=adv_li_st_2">Alexandra Daddario</a>, 
<a href="/name/nm1231899/?ref_=adv_li_st_3">Priyanka Chopra</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="131063" name="nv">131,063</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="58,060,186" name="nv">$58.06M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3532216"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3532216/?ref_=adv_li_i"> <img alt="American Made" class="loadlate" data-tconst="tt3532216" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTUxNzUwMjk1Nl5BMl5BanBnXkFtZTgwNDkwODI1MjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">44.</span>
<a href="/title/tt3532216/?ref_=adv_li_tt">American Made</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">18</span>
<span class="ghost">|</span>
<span class="runtime">115 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Biography, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.2" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.2</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3532216" id="urv_tt3532216">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3532216">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3532216|imdb|7.2|7.2|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.2/10 (126,633 votes) - click stars to rate">
<meta content="7.2" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="126633" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 100.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3532216/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">65        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    The story of Barry Seal, an American pilot who became a drug-runner for the CIA in the 1980s in a clandestine operation that would be exposed as the Iran-Contra Affair.</p>
<p class="">
    Director:
<a href="/name/nm0510731/?ref_=adv_li_dr_0">Doug Liman</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000129/?ref_=adv_li_st_0">Tom Cruise</a>, 
<a href="/name/nm1727304/?ref_=adv_li_st_1">Domhnall Gleeson</a>, 
<a href="/name/nm0942792/?ref_=adv_li_st_2">Sarah Wright</a>, 
<a href="/name/nm0687146/?ref_=adv_li_st_3">Jesse Plemons</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="126633" name="nv">126,633</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="51,342,000" name="nv">$51.34M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt6468322"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt6468322/?ref_=adv_li_i"> <img alt="La casa de papel" class="loadlate" data-tconst="tt6468322" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMzBlY2QzNzYtMWU1NS00NjFkLWJiMzItYmM3YTc4MDFjNDQwXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">45.</span>
<a href="/title/tt6468322/?ref_=adv_li_tt">La casa de papel</a>
<span class="lister-item-year text-muted unbold">(2017– )</span>
</h3>
<p class="text-muted">
<span class="runtime">70 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Crime, Mystery            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt6468322" id="urv_tt6468322">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt6468322">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt6468322|imdb|8.6|8.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.6/10 (119,439 votes) - click stars to rate">
<meta content="8.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="119439" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 120.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt6468322/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
</div>
<p class="text-muted">
    A group of very peculiar robbers assault the Factory of Moneda and Timbre to carry out the most perfect robbery in the history of Spain and take home 2.4 billion euros.</p>
<p class="">
            
    Stars:
<a href="/name/nm2216549/?ref_=adv_li_st_0">Úrsula Corberó</a>, 
<a href="/name/nm1523587/?ref_=adv_li_st_1">Itziar Ituño</a>, 
<a href="/name/nm1486647/?ref_=adv_li_st_2">Álvaro Morte</a>, 
<a href="/name/nm1699346/?ref_=adv_li_st_3">Alba Flores</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="119439" name="nv">119,439</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3371366"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3371366/?ref_=adv_li_i"> <img alt="Transformers: The Last Knight" class="loadlate" data-tconst="tt3371366" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">46.</span>
<a href="/title/tt3371366/?ref_=adv_li_tt">Transformers: The Last Knight</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">P13</span>
<span class="ghost">|</span>
<span class="runtime">154 min</span>
<span class="ghost">|</span>
<span class="genre">
Action, Adventure, Sci-Fi            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="5.2" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>5.2</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3371366" id="urv_tt3371366">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3371366">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3371366|imdb|5.2|5.2|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 5.2/10 (115,654 votes) - click stars to rate">
<meta content="5.2" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="115654" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 72.8px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">5.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3371366/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore unfavorable">27        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A deadly threat from Earth's history reappears, and a hunt for a lost artifact takes place between Autobots and Decepticons, while Optimus Prime encounters his creator in space.</p>
<p class="">
    Director:
<a href="/name/nm0000881/?ref_=adv_li_dr_0">Michael Bay</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0000242/?ref_=adv_li_st_0">Mark Wahlberg</a>, 
<a href="/name/nm0000164/?ref_=adv_li_st_1">Anthony Hopkins</a>, 
<a href="/name/nm0241049/?ref_=adv_li_st_2">Josh Duhamel</a>, 
<a href="/name/nm2652095/?ref_=adv_li_st_3">Laura Haddock</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="115654" name="nv">115,654</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="130,168,683" name="nv">$130.17M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5290382"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5290382/?ref_=adv_li_i"> <img alt="Mindhunter" class="loadlate" data-tconst="tt5290382" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMzNkZmNmZjMtZWI5OC00MzdiLTgxMjAtZWY2ZTIwMWM2Yzc2XkEyXkFqcGdeQXVyMjM5NDQzNTk@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">47.</span>
<a href="/title/tt5290382/?ref_=adv_li_tt">Mindhunter</a>
<span class="lister-item-year text-muted unbold">(2017– )</span>
</h3>
<p class="text-muted">
<span class="runtime">60 min</span>
<span class="ghost">|</span>
<span class="genre">
Crime, Drama, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.5" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.5</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5290382" id="urv_tt5290382">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5290382">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5290382|imdb|8.5|8.5|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.5/10 (114,683 votes) - click stars to rate">
<meta content="8.5" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="114683" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 119px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5290382/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
</div>
<p class="text-muted">
    Set in the late 1970s, two FBI agents are tasked with interviewing serial killers to solve open cases.</p>
<p class="">
            
    Stars:
<a href="/name/nm2676147/?ref_=adv_li_st_0">Jonathan Groff</a>, 
<a href="/name/nm0564697/?ref_=adv_li_st_1">Holt McCallany</a>, 
<a href="/name/nm1396022/?ref_=adv_li_st_2">Anna Torv</a>, 
<a href="/name/nm2193120/?ref_=adv_li_st_3">Hannah Gross</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="114683" name="nv">114,683</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt4116284"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt4116284/?ref_=adv_li_i"> <img alt="The Lego Batman Movie" class="loadlate" data-tconst="tt4116284" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZTgwOTAyNzU3MDI@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">48.</span>
<a href="/title/tt4116284/?ref_=adv_li_tt">The Lego Batman Movie</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">U</span>
<span class="ghost">|</span>
<span class="runtime">104 min</span>
<span class="ghost">|</span>
<span class="genre">
Animation, Action, Comedy            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.3" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.3</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt4116284" id="urv_tt4116284">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt4116284">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt4116284|imdb|7.3|7.3|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.3/10 (113,579 votes) - click stars to rate">
<meta content="7.3" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="113579" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 102.2px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.3</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt4116284/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">75        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick.</p>
<p class="">
    Director:
<a href="/name/nm0003021/?ref_=adv_li_dr_0">Chris McKay</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0004715/?ref_=adv_li_st_0">Will Arnett</a>, 
<a href="/name/nm0148418/?ref_=adv_li_st_1">Michael Cera</a>, 
<a href="/name/nm0206257/?ref_=adv_li_st_2">Rosario Dawson</a>, 
<a href="/name/nm0000146/?ref_=adv_li_st_3">Ralph Fiennes</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="113579" name="nv">113,579</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="175,750,384" name="nv">$175.75M</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt5834204"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt5834204/?ref_=adv_li_i"> <img alt="The Handmaid's Tale" class="loadlate" data-tconst="tt5834204" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BMTU0MTI0MDAyM15BMl5BanBnXkFtZTgwMDg5MzYyNTM@._V1_UY98_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">49.</span>
<a href="/title/tt5834204/?ref_=adv_li_tt">The Handmaid's Tale</a>
<span class="lister-item-year text-muted unbold">(2017– )</span>
</h3>
<p class="text-muted">
<span class="runtime">60 min</span>
<span class="ghost">|</span>
<span class="genre">
Drama, Sci-Fi, Thriller            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="8.6" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>8.6</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt5834204" id="urv_tt5834204">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt5834204">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt5834204|imdb|8.6|8.6|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 8.6/10 (109,892 votes) - click stars to rate">
<meta content="8.6" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="109892" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 120.4px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">8.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt5834204/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
</div>
<p class="text-muted">
    Set in a dystopian future, a woman is forced to live as a concubine under a fundamentalist theocratic dictatorship.</p>
<p class="">
            
    Stars:
<a href="/name/nm0005253/?ref_=adv_li_st_0">Elisabeth Moss</a>, 
<a href="/name/nm1540404/?ref_=adv_li_st_1">Max Minghella</a>, 
<a href="/name/nm0115760/?ref_=adv_li_st_2">Amanda Brugel</a>, 
<a href="/name/nm2088803/?ref_=adv_li_st_3">Yvonne Strahovski</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="109892" name="nv">109,892</span>
</p>
</div>
</div>, <div class="lister-item mode-advanced">
<div class="lister-top-right">
<div class="ribbonize" data-caller="filmosearch" data-tconst="tt3521126"></div>
</div>
<div class="lister-item-image float-left">
<a href="/title/tt3521126/?ref_=adv_li_i"> <img alt="The Disaster Artist" class="loadlate" data-tconst="tt3521126" height="98" loadlate="https://m.media-amazon.com/images/M/MV5BOGNkMzliMGMtMDI5Ni00OTZkLTgyMTYtNzk5ZTY1NjVhYjVmXkEyXkFqcGdeQXVyNTAzMTY4MDA@._V1_UX67_CR0,0,67,98_AL_.jpg" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/large/film-184890147._CB470041630_.png" width="67"/>
</a> </div>
<div class="lister-item-content">
<h3 class="lister-item-header">
<span class="lister-item-index unbold text-primary">50.</span>
<a href="/title/tt3521126/?ref_=adv_li_tt">The Disaster Artist</a>
<span class="lister-item-year text-muted unbold">(2017)</span>
</h3>
<p class="text-muted">
<span class="certificate">(Banned)</span>
<span class="ghost">|</span>
<span class="runtime">104 min</span>
<span class="ghost">|</span>
<span class="genre">
Biography, Comedy, Drama            </span>
</p>
<div class="ratings-bar">
<div class="inline-block ratings-imdb-rating" data-value="7.4" name="ir">
<span class="global-sprite rating-star imdb-rating"></span>
<strong>7.4</strong>
</div>
<div class="inline-block ratings-user-rating">
<span class="userRatingValue" data-tconst="tt3521126" id="urv_tt3521126">
<span class="global-sprite rating-star no-rating"></span>
<span class="rate" data-no-rating="Rate this" data-value="0" name="ur">Rate this</span>
</span>
<div class="starBarWidget" id="sb_tt3521126">
<div class="rating rating-list" data-auth="" data-ga-identifier="" data-starbar-class="rating-list" data-user="" id="tt3521126|imdb|7.4|7.4|||advsearch|title" itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating" title="Users rated this 7.4/10 (108,369 votes) - click stars to rate">
<meta content="7.4" itemprop="ratingValue"/>
<meta content="10" itemprop="bestRating"/>
<meta content="108369" itemprop="ratingCount"/>
<span class="rating-bg"> </span>
<span class="rating-imdb" style="width: 103.6px"> </span>
<span class="rating-stars">
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
<a href="/register/login?why=vote&amp;ref_=tt_ov_rt" rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating"><span class="value">7.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel"><a href="/title/tt3521126/vote?v=X;k=" rel="nofollow" title="Delete"><span>X</span></a></span>
 </div>
</div>
</div>
<div class="inline-block ratings-metascore">
<span class="metascore favorable">76        </span>
        Metascore
            </div>
</div>
<p class="text-muted">
    When <a href="/name/nm0802995">Greg Sestero</a>, an aspiring film actor, meets the weird and mysterious <a href="/name/nm1382072">Tommy Wiseau</a> in an acting class, they form a unique friendship and travel to Hollywood to make their dreams come true.</p>
<p class="">
    Director:
<a href="/name/nm0290556/?ref_=adv_li_dr_0">James Franco</a>
<span class="ghost">|</span> 
    Stars:
<a href="/name/nm0290556/?ref_=adv_li_st_0">James Franco</a>, 
<a href="/name/nm2002649/?ref_=adv_li_st_1">Dave Franco</a>, 
<a href="/name/nm0310966/?ref_=adv_li_st_2">Ari Graynor</a>, 
<a href="/name/nm0736622/?ref_=adv_li_st_3">Seth Rogen</a>
</p>
<p class="sort-num_votes-visible">
<span class="text-muted">Votes:</span>
<span data-value="108369" name="nv">108,369</span>
<span class="ghost">|</span> <span class="text-muted">Gross:</span>
<span data-value="21,120,616" name="nv">$21.12M</span>
</p>
</div>
</div>]
>>> first_movie.div
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    first_movie.div
NameError: name 'first_movie' is not defined
>>> first_movie.div,
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    first_movie.div,
NameError: name 'first_movie' is not defined
>>> first_movie.a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    first_movie.a
NameError: name 'first_movie' is not defined
>>> first_movie
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    first_movie
NameError: name 'first_movie' is not defined
>>> first-movie.div
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    first-movie.div
NameError: name 'first' is not defined
>>> first_movie.div
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    first_movie.div
NameError: name 'first_movie' is not defined
>>> first_name = first_movie.h3.a.text

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    first_name = first_movie.h3.a.text
NameError: name 'first_movie' is not defined
>>> first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
NameError: name 'first_movie' is not defined
>>> first_movie_containers
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    first_movie_containers
NameError: name 'first_movie_containers' is not defined
>>> first_movie(div)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    first_movie(div)
NameError: name 'first_movie' is not defined
>>> movie_container.div
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    movie_container.div
NameError: name 'movie_container' is not defined
>>> movie_containers.div
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    movie_containers.div
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python36-32\lib\site-packages\bs4\element.py", line 1620, in __getattr__
    "ResultSet object has no attribute '%s'. You're probably treating a list of items like a single item. Did you call find_all() when you meant to call find()?" % key
AttributeError: ResultSet object has no attribute 'div'. You're probably treating a list of items like a single item. Did you call find_all() when you meant to call find()?
>>> find_all
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    find_all
NameError: name 'find_all' is not defined
>>> find_all(movie_containers)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    find_all(movie_containers)
NameError: name 'find_all' is not defined
>>> list = first_movie.div
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list = first_movie.div
NameError: name 'first_movie' is not defined
>>> find_all('50')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    find_all('50')
NameError: name 'find_all' is not defined
>>> 
