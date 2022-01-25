

# All Variables used in tests-----------------------
from ipaddress import ip_address


html_1 = """<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>"""
html_2 = """<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>
<li style="-moz-float-edge: content-box">... that the three cities of the <b><a href="/wiki/West_Triangle_Economic_Zone" title="West Triangle Economic Zone">West Triangle Economic Zone</a></b> contribute 40% of Western China's GDP?</li>
<li style="-moz-float-edge: content-box">... that <i><a href="/wiki/Kismet_(1943_film)" title="Kismet (1943 film)">Kismet</a></i>, directed by <b><a href="/wiki/Gyan_Mukherjee" title="Gyan Mukherjee">Gyan Mukherjee</a></b>, ran at the <a href="/wiki/Roxy_Cinema_(Kolkata)" title="Roxy Cinema (Kolkata)">Roxy, Kolkata</a>, for 3 years and 8 months?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Vauix_Carter" title="Vauix Carter">Vauix Carter</a> both coached and played for the <b><a href="/wiki/1882_Navy_Midshipmen_football_team" title="1882 Navy Midshipmen football team">1882 Navy Midshipmen football team</a></b>?</li>
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Zhu_Chenhao" title="Zhu Chenhao">Zhu Chenhao</a> was sentenced to <a href="/wiki/Slow_slicing" title="Slow slicing">slow slicing</a> for leading the <b><a href="/wiki/Prince_of_Ning_rebellion" title="Prince of Ning rebellion">Prince of Ning rebellion</a></b> against the <a href="/wiki/Ming_Dynasty" title="Ming Dynasty">Ming Dynasty</a> <a href="/wiki/Zhengde_Emperor" title="Zhengde Emperor">emperor Zhengde</a>?</li>
<li style="-moz-float-edge: content-box">... that <b><a href="/wiki/Mirza_Adeeb" title="Mirza Adeeb">Mirza Adeeb</a></b> was a prominent modern Pakistani <a href="/wiki/Urdu" title="Urdu">Urdu</a> playwright whose later work focuses on social problems and daily life?</li>
<li style="-moz-float-edge: content-box">... that in <i><b><a href="/wiki/La%C3%9Ft_uns_sorgen,_la%C3%9Ft_uns_wachen,_BWV_213" title="Lat uns sorgen, lat uns wachen, BWV 213">Die Wahl des Herkules</a></b></i>, Hercules must choose between the good cop and the bad cop?<br style="clear:both;" />
<div style="text-align: right;" class="noprint"><b><a href="/wiki/Wikipedia:Recent_additions" title="Wikipedia:Recent additions">Archive</a></b>  <b><a href="/wiki/Wikipedia:Your_first_article" title="Wikipedia:Your first article">Start a new article</a></b>  <b><a href="/wiki/Template_talk:Did_you_know" title="Template talk:Did you know">Nominate an article</a></b></div>
</li>"""
html_3 = """<ul>
<li style="-moz-float-edge: content-box">Former Italian Prime Minister <a href="/wiki/Silvio_Berlusconi" title="Silvio Berlusconi">Silvio Berlusconi</a> <i>(pictured)</i> is <b><a href="/wiki/Silvio_Berlusconi_underage_prostitution_charges" title="Silvio Berlusconi underage prostitution charges">found guilty</a></b> of paying for sex with an underage prostitute.</li>
<li style="-moz-float-edge: content-box">In sports car racing, the <b><a href="/wiki/2013_24_Hours_of_Le_Mans" title="2013 24 Hours of Le Mans">24 Hours of Le Mans</a></b>, won by <a href="/wiki/Tom_Kristensen" title="Tom Kristensen">Tom Kristensen</a>, <a href="/wiki/Allan_McNish" title="Allan McNish">Allan McNish</a> and <a href="/wiki/Lo%C3%AFc_Duval" title="Loc Duval">Loc Duval</a>, is marred by the death of <b><a href="/wiki/Allan_Simonsen_(racing_driver)" title="Allan Simonsen (racing driver)">Allan Simonsen</a></b>.</li>
<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_Alberta_floods" title="2013 Alberta floods">Flooding</a></b> in <a href="/wiki/Alberta" title="Alberta">Alberta</a>, Canada, results in at least three deaths and the evacuation of thousands.</li>
<li style="-moz-float-edge: content-box"><b><a href="/wiki/2013_North_India_floods" title="2013 North India floods">Flash floods and landslides</a></b> in <a href="/wiki/Uttarakhand" title="Uttarakhand">Uttarakhand</a> and <a href="/wiki/Himachal_Pradesh" title="Himachal Pradesh">Himachal Pradesh</a> in India kill more than <span class="nowrap">1,000 people</span> and trap more than 20,000.</li>
<li style="-moz-float-edge: content-box">In <a href="/wiki/Basketball" title="Basketball">basketball</a>, the <a href="/wiki/Miami_Heat" title="Miami Heat">Miami Heat</a> defeat the <a href="/wiki/San_Antonio_Spurs" title="San Antonio Spurs">San Antonio Spurs</a> to win the <b><a href="/wiki/2013_NBA_Finals" title="2013 NBA Finals">NBA Finals</a></b>.</li>
</ul>"""

string_1 = """satisfied)profit profit'container fashion.profit'egg profit-ms profit_unimportant leaf(profit profit.fall bear_profit offend_profit audience(profit'manager
interested(lack interested.normal slowly-interested interested'schedule untidy,interested sign(interested interested_tube boil(interestedthey interestedconfined pretty.interested,stressed
journalist)profit(cat crop(profit class)profit altogether(profit pound,profit-assure strange'profit kindly'profit-over profit)potentially credit,profit-homework profit.devote
goldclimbing extent_gold manage(gold.relaxing scream'gold insect_gold look'gold-town conventional-gold noticeablegoldpromptly intention.gold gold.make
organizationinterested'important interested-climb bankinterested picture.interested irritate'interested,variation encouragementinterested interested-beautiful noise-interested)luggage interested.variation cellphone-interested
media(profit staff-profit search-profit foreignprofit my'profit_find profit'ct disappointment'profit.climb blackprofit profit-have tin.profit
promptly(adult_pronunciation through)adult adult)repair hand)adult section(adult(difficult interval_adult.retired adult_task adult)further adult'sexual faith_adult
after)profit trick,profit profit)electronic profit'grab lake'profit_price avoid'profit'chop whistle,profit.confined profitoccasion combination,profit'direction curb_profit)straight
profit)spare profit.aspect floodprofit-care profitlocate profit-fundamental dog,profitgroup profitadequate petrol)profit-object profitreasonable profit'female
capture.gold actively.gold.separation gold.cold gold)particular gold)faithful frame,gold glue.gold gold.model sail-gold.nature lane(gold)sink
spirit.adult adult(basis adult-rush adult,get adult)make waist,adult.quiet throat(adult reality(adult adult)rob adult'closet
way-profit.go seriously)profit.desert bitter.profit atomprofit,interior cheque,profit(hatred publication,profit improve,profit variation_profit_good rubber(profitblue profit)quality
resource-profit profitwing profit'absence fever_profit profit-chief profit.goal entertainment'profit)neighbourhood gentleman,profit assume,profit_understanding hello-profit
adult_fever stupid-adult,expense adultcentury create,adult visionadult perfectlyadult instead,adult south_adult.ice map,adult adult-blood
coldlyinterested.nevertheless countyinterested)educated unlikely.interested_landscape interested-themselves interested_homework pension.interested annoyinterested(again mid_interested interested_weapon hammer_interested(swollen
themselves,profit weakness'profit insert_profit)record regulation_profit profit-beneath sharp)profit_wrapping obvious-profit.project remind'profit.tendency giveprofit_lie profit'confidently
avoid'profit.resort contract)profit float.profit complexprofit profit,save profit.staff profit_expensive mark'profit(brain profit,mg indirect.profit-apartment
profit-virtually rough,profit,excuse profit)pool profit-thickness hero_profit profit'lose profit(tea profit(re earth,profit)breathing restriction)profit
determined'profit,collapse poetry)profit profit.case profit,cap profit.burn profit-stock flour)profit_construction profit,alone profitinfection flight'profit
recover'interested,persuade suck)interested interested'film engaged(interested'traditionally pollution(interested'task interested)give working_interested interested-relaxing ininterested certainly.interested.paper
till,profit)wander aged,profit profit-patient profit-cost profit,head research(profit method_profit)mid annual_profit briefly(profit,spoon along)profit
offence,adult adult.article granddaughter.adult dentist)adult-mr thank-adult commercial(adult draft.adult'document licence-adult which.adult.well unload'adult.tire
gold'statue make.gold whilstgoldrefrigerator themselves_gold goldexamination furniture.gold cat'goldamazed wound)gold_department gold'tuesday potato(gold_wrap
serious_adult-wrap real-adult'warm exactly)adult adultengine chair-adult button-adult,take adult'afternoon adult.regulation impose-adult adultconsiderable
uncontrolled'adult,help division,adultthorough corner,adult_equipment amuse_adult except-adult_cloth language.adult attorney.adult boot_adult)permanent rely,adult southernadult
profit(achievement kilometre.profit each)profit profit'obtain class_profit-few south(profit,yours profitrace profit_contract profit(willingness profit(capture
nutprofit.deliberately profitwhich magic.profit sweater)profit profit)translation profit_wash profit)barrier profit-decorative c(profit proportion-profitpresence
increaseadult addition_adult)come separated(adult providedadult prepare_adult)shame lonely-adult complete.adult.after adult)forgive hire'adultmuch religion'adult'arms
suited)adult salary'adult adultsafety western-adult_technique zeroadult(humorous adult.drugstore adult_theme adult_stranger adulttoy technology,adult
amusing(adult fire.adult_suffer hard)adult upon)adult noadult'until spelling)adult-glasses adult-brave throw'adult yours.adult all-adult(wooden
interestedconference interested'necessarily interested'visitor publicity,interested roof)interestedlunch etc_interestedapply curl'interestedtiny considerable_interested containinterested interested_earth
depressing-adult rid-adult,agent pretend_adult_fancy adult-remain orange_adult take-adult onlyadult(be adult.sewing adult(decrease pick'adult)physical
interestedrid park,interested public-interested'woman fork,interested)thing would(interested)pan expected-interested interested.illegally interestedplastic enjoyment(interested interested_trace
ruin-interested'basic interestedbacteria interested(sheet interested)contrasting interested)presentation interested_prior nuclear,interested bite.interested-never interested-reception mysterious-interested
interested)insist our_interested pace(interested,fish interested.in interestedretirement interior'interested theme-interested interested(appointment interested-none pollution)interested
adult,possible adult.gentle adult(reduce willingness,adult hideadult adult.luggage fame.adult beach.adult adult_plate fly,adult
profita adequateprofit achieve)profit_style profit_expression central,profit sweep.profit indirectly(profit sound_profit.academic profitcontinue fold)profit_woman
interested_skilled interested'engineering interested_objective signalinterested'unhappiness fee)interested wholeinterested)effort interested)depress novel)interested solution)interested'enjoyable awkwardly(interested
adult.congratulations sing_adult adult)voice political.adult adult-knee adult(miss enough)adult adult,satisfying adult)cheque ordinary-adult)expensive
historical)adult_representative student(adult green_adult confirm_adult.deaf adult_proportion shiny_adult)counter unemployed,adult.foot friendly-adult adult)pig oppositeadult"""

sub_word_1 = "gold"
sub_word_2 = "profit"
sub_word_3 = "adult"
sub_word_4 = "interested"

username_1 = "_0898989811abced_"
username_2 = "_abce"
username_3 = "_09090909abcD0"
username_4 = "_455894903590720027BFYblVbWxrlDISuncMjQXwwwQ_"
username_5 = "_DevgMmdgyqsClabHIM"

ip_address_1 = "1051:1000:4000:abcd:5:600:300c:326b"
ip_address_2 = "222.231.113.64"
ip_address_3 = "Test"
ip_address_4 = "1050:10:0:10:5:600:300c:326a"

string_2 = """colourfuture saturday.future face_future(anxiety obtain.future surroundings'futurerefrigerator alone)futurecomparison wine-future,tight futureimpatient bodyfuture excite(future(grandfather
other(stick star,stick stick)critical stick(debt cheek_stick.representative serious(stick stick(sticky stick)chew dress)stick go_stick(furniture
occupy-tip repeat_tip pace)tip,riding catch(tip protect)tip dirt(tip(imagination commitment-tip(infected altogether.tip politically'tip anniversarytip
secure,tip board(tip)fever pile(tip_alphabetically remote)tip aloud(tip defend'tip_religious bottletip feeltip_unhappiness tip'swallow tear.tip
channel(hobby bus)channel(drunk soul(channel channel,take pour_channel-removal order(channel_outline channel.mirror channel-breakfast creature(channel,smoking toilet_channel-cd
cleanchannel hotel.channel govern'channel channel-check inquiry.channel)eat estatechannelconsumer channeluniverse crop-channel(qualification massive,channel parliamentchannel
tear(fund violently,tear)security sillytear(minimum property-tear_acquire steal(tear tear(include grow'tear)court tear'mountain tear'block tear,persuade
enjoyable(tear(usually climbing-tear jumptear cause.tear,file peace.tear depressed(tear envelope)tear-owe room_tear.pleasure choose_tear outer_tear,machinery
mine)realize beach)realize,take realize-gold camera_realizemouse anyone_realize-chemical wounded-realize'sheep superior_realizeoccupied construct(realize base,realize realize-hospital
fighting'channel industrial)channel-instead channel.traffic poetry-channel_bar channelnature cow_channel,in channelwashing channelmanner channel,root stay'channel(dollar
future)aircraft status)future continuously)future wild'future'land bore_future float.future_bandage absent'future'model ability)future future(a definition'future)admit
unconscious_tear oddlytearmood basic.tear tear.accuse tear-knitting tear.instead daily)tear extraordinary'tear.downwards tear-ultimate thursdaytear
divide)realizespring disappointed(realize realizefebruary realize'visit till'realize populationrealize realize.offer reform.realize-get himself,realize.window word-realizedressed
honestly)realize'nowhere invest)realize(into realize.contribute scared,realize sound-realizedue favour)realize realizeall includingrealize.purely camprealize colleague'realize.elbow
furnituretear.totally tear.tomato tear,guide advice_tear_injured season'tear sudden,tear tonight.tear_restricted old_tear,curve tear_upon tearsession
futureconfront future)i future(spare northern,future(elegant future'hang future.improvement milligram)future.vote future(modern boat,future'wrapping photography,future
in'realize realize-blonde underwaterrealize.magazine realize(pleasure bake_realize seem(realize.chart by-realize realize-entrance realize.regulation damp-realize
artistic'realize)argument opportunity_realizewillingness realize)everything realize.equally realize'analysis cancel.realize-confine idea'realize friend,realize,cellphone realize-youth re)realize
tip'power article,tip-fridge tip)television impacttip effective-tip spacetipdisturbing tip'oh tip,fun prisoner.tip.packet noisetiplaw
stick.attractive somebodystick stick'new throat.stick,deep stick(outdoors stick.km may.stickexclude stick,arrangement stick(deeply stick(ultimately
contract(stick weekend,stick,shell targetstick stick)labour cottage-stick(equal sticksincere discuss-stick debt_stick relation)stick put_stick
victory,stick stick.employment loudly_stick stick.normally enter)stick_ideally contract)stick-poetry facility,stick fever(stick stick.delivery failure'stick
response(stick(access stick'blonde stick_judgement stickloudly a'stick silkstick,worship danger,stick cigarette)stick.everywhere stick)war stick-hero
minute,tear-cousin temporarily_tear determined,tear greytear tear'interrupt tear(profession goodbye)tear steady)tear(restricted employer,tear tear-extent
jewellery(future)furniture expose,future,govern future)of future(pronounce future-big future(crazy mental'future'ingredient work,future pass_future(generous step,future
establish-tip_humour small-tipmidday tip.against tip.breakfast occasionally.tip chequetip'phone hard)tip artificiallytip tip(employment because'tip.grocery
remarkably_stick miss'stick similarstick seat,stick(zero mind.stick.imagine joy'stick,wave yellow'stick)sudden wake.stick stick,really stick,preference
wife-realize pop)realize'sight glass)realize realize.aid realize-stair undo,realize realize.occur feel_realize,odd display'realize realize,represent
in'stick)passing east-stickdriver stick-admit stick-hunt each)stick.represent professor_stickgrandchild working-stick(paint decorative(stick)advertise stick(weather unlike(stick
mentally'tip(ask tip,exaggerate label)tip arrow)tipsock tip'look tip_euro tip)engineering success(tip tipdead market_tip
educate(tip rush,tip tip,stair tip)class proceed.tip tipfreedom display)tip.recall ingredient-tip pick_tip(increasingly tip_convince
taste(tear cow)tear'an tear.grateful practical.tear tearitself tear.disk latest)tearclub tearlook senator,tear instead(tear
tear(continue emotional'tear tear(emphasize spice'tear indoors.tear tear_resist crushtear.morally tear.unemployment achieve,tear institution,tear_low
tear.machinery tip_tear_deserted diet_tear familiar'tear)swear clothes(tear tear-innocent tear,equipment tear,spoon tear_none creature'tear
stick.membership stick_kill counter.stick'continue our,stick movie,stick sit,stick_something stick-importance fast.stick admiration_stick.east removal'stick-unable
tear(snow litre_tear'attention rain)tear,underground alarm.tear(impressed insist_tear triangle-tear tear_pocket saturday.tear cycling.tear,reply behalf'tear
tear-trick hotel)tear(half educate.tear(police tear-cancer independent)tear tear.quiet offend-tearmost tearindustrial initiative(tear pink_tear
sail.futurelucky futuremidday future(each accompany)future)singing future-attractive define,future neat,future future-guess on(future_desk criticismfuture
quite_stick)fear stick.measure classic(stick varied_stick-division race)stick illustrate.stick)unwilling tonne-stick stickbreak common(stick phrasestick
association-tip switch,tip'sadness have)tip concentrate-tip tipus tip-element fishing_tip(breast offencetip.irritating tip,text sharply_tip
july)channel a,channel.other preparation(channel,upwards extensive_channel-collect the_channel fearchannel step,channel belong(channel-good unlike(channel channel-practical
realize)injured realize(access realize(lunch adjust-realize'beard row-realize,connection finely(realize(needle weight)realize institution_realizealongside breed_realize'preserve in.realize
tipwelcome closet-tip.self fan-tip tip(onto visitor.tip temperature_tip classroom,tip tip.representative tip,pick surprising)tiplayer
stick)president fame)stick reachstick.guest specific(stick'pause rarely'stick'flavour noticestick earth'stick frozen(stick residentstick.grand standstick(birth
unpleasantrealizepilot realize(mix realize,degree coat)realize realizesuit atmosphere_realize self,realize pick,realize,the runnerrealize violence,realize
future(file disapprovefuture_environment priest-future future,bath future(pull future'competition future(throw future(north interpretationfuture,secretary boss'future
stick(and stick)photocopy stick)reserve tiestick stick.which stick,shall island,stick substantial)stick stick_hungry stick,mixed
realize-hungry realize_none realize)anxiously burn_realize)skilfully realizeengineer castle(realize continent,realize(far failure(realize sum,realize league'realize_bin
tip_exactly blame)tippowerful tip,justice tip.your singer)tip tip,amazing knee'tip tip,original ridetip flying-tip
tip,pose cooker_tip finger,tip tip,deserve purple,tip tip_hurry tip,expose bit-tip.drama tip-insult crazy'tip
enter.tearplan bound.tear reform,tear,lie tear,approximate tearrequest curiously.tear sign.tear)control tear,sample ctear approve'tear
stick,brain unwilling'stickacross stick-item takestick stick(already flavour,stick)teacher stick_armed stick'intended stick_less stick)knee
victory)channel.ok grandsonchannel channel,automatically tomato'channel)deliver enthusiasm)channel_distance channel.before yours)channel,account channel(hard once'channel channel(often
pronounce_channel myself)channel sticky,channelwater channel)beat channel'ability host,channel.nurse engage_channel surroundings'channel channel,lie idea.channel
future)dinner future'boss always.futurewind sympathy)future-overcome future_toe futureupset future,diet hungry_future steerfuture_relate worshipfuture'machinery
realize.infect weekly.realize_difficult realize-gift company.realize eat-realize.diagram previously-realize reward_realize inevitable-realize formal'realize rerealize
potentially-tip)oppose devoted_tip(june jacket_tip(voice tip)last mom(tip.ridiculous certainly(tip tip(go plus_tip interpret)tip.wild lacking'tip
studio.channel element-channel range-channel(outstanding channelsurprise stair.channel reckon(channel,bent dear(channel quit-channel channel_anything channel'weapon
public_stick-the stick_rounded millimetre.stick(initiative mall(stick opposed_stick,give state-stick stick(unwilling explanation'stick crucial(stick stick.anger
tear'generate faucettear(switch sack,tear tear(autumn stonetear descriptionteartogether tear)km court'tear tear)imagination tear-irritating"""

word_1 = "tip"
word_2 = "channel"
word_3 = "tear"
word_4 = "stick"


string_3 = """Adventure
Send a letter to the editor about the content of the Adventure website.
mpotts@ngs.org
Advertising
Why not sponsor an online feature?
jbmccorm@ngs.org
The Complete National Geographic
Use this help form to contact us with comments or support questions regarding The Complete National Geographic on DVD or hard drive.
CNG Help Form
Customer Service: Magazine Subscriptions
Send questions regarding your subscriptions. Check on delivery, expiration dates, or other concerns. Inquiries about National Geographic, National Geographic Kids, and Traveler can be sent to this email address. Customer service is also available online at ngsline@customersvc.com.
Digital Magazine Subscriptions
For questions about digital subscriptions to National Geographic magazine (iPad, Nook, Kindle, or Zinio) email us at ngsdigital@customersvc.com or call 1-800-895-2068. You can also read the digital FAQs online.
Donating to National Geographic
Please contact us at givinginfo@ngs.org or call +1 202 862 8638 with any questions regarding your donation, or how to make a donation in support of the Society's work in exploration, research, and education. Thank you for your support!
Frequently Asked Questions
Find answers to your questions here.
http://www.nationalgeographic.com/faq/
Games
For questions about downloadable games and Plan It Green Live, please write to:
askngs@nationalgeographic.com and put "Attn: Games" in the subject line.
Genographic Project
Send us your questions regarding the Genographic Project.
genographic@ngs.org
Genographic Project en espaï¿½ï¿½ol
Envienos en espaï¿½ï¿½ol sus preguntas sobre el Proyecto Genographic.
genographicespanol@ngs.org
Mobile Applications and More
Email us with comments or support questions regarding our content for iPhone, iPad, Android, Windows Mobile 7, and more: apps@ngs.org.
For magazine app and digital subscription queries email us at ngsdigital@customersvc.com or call 1-800-895-2068.
National Geographic Channel
Send comments or questions regarding our television programming.
feedback@natgeotv.com
National Geographic Expeditions
For more information or to reserve your space, call toll-free 1-888-966-8687, or reserve online at nationalgeographicexpeditions.com.
For email inquiries use this form.
National Geographic Magazine
Send a letter to the Editor about the content of National Geographic magazine. Letters will be considered for the monthly Forum column.
ngsforum@nationalgeographic.com
National Geographic Maps
Contact us with questions about our maps.
maps@ngs.org
Photography: Stock Photography
National Geographic Stock's photography collection offers the best in rights managed and royalty free wildlife, travel, landscape and lifestyle photographs available for professional editorial and commercial licensing.
stock@ngs.org
Photography: Commercial Assignments
National Geographic Assignment represents international commercial photographers specializing in lifestyle, adventure, travel, and landscape photography. Online portfolios are available.
ngassignment@ngs.org
Photography: Prints
You can order beautiful National Geographic prints for your home or as a great gift. Browse through our collection.
News
Send comments, questions or concerns regarding the National Geographic News site.
newsdesk@nationalgeographic.com
Public Relations
Send press inquiries here.
pressroom@ngs.org
Speakers Bureau
Send inquiries about having a National Geographic photographer, adventurer, explorer, or scientist speak at your next event.
speakers@ngs.org
TOPO! Digital Maps
Send us your product and technical support quesions.
topo@ngs.org
Traveler Magazine
Send a letter about Traveler magazine.
Traveler@ngs.org
Your Shot & Your Shot Puzzles
Help Form
Frequently Asked Questions
Miscellaneous
Not sure where to send your question? Weï¿½ï¿½ï¿½ll pass it to the proper department. Please keep in mind that the high volume of mail does not allow us to send everyone a personal answer.
askngs@nationalgeographic.com"""

string_4 = """E-MAIL ADDRESSES OF GMs AND DRMs ON IR
RLY	GM E-Mail	Division	DRM E-Mail
CR	gm@cr.railnet.gov.in	Mumbai	drm@bb.railnet.gov.in
Bhusawal	drm@bsl.railnet.gov.in
Pune	drm@pa.railnet.gov.in
Nagpur	drm@ngp.railnet.gov.in
Solapur	drm@sur.railnet.gov.in
ER 	gm@er.railnet.gov.in	Howrah	drmhwh@er.railnet.gov.in
Sealdah	drmsdah@er.railnet.gov.in
Asansol	drmasn@er.railnet.gov.in
Malda	drmmldt@er.railnet.gov.in
ECR 	gm@ecr.railnet.gov.in	Danapur	drmdnr@ecr.railnet.gov.in
Dhanbad	drmdhn@ecr.railnet.gov.in
Mughalsarai	drmmgs@ecr.railnet.gov.in
Samastipur	drmspj@ecr.railnet.gov.in
Sonpur	drmsee@ecr.railnet.gov.in
ECoR    	gm@eastcoastrailway.gov.in  	Khurda Road	drmkur@eastcoastrailway.gov.in
Sambalpur	drmsbp@eastcoastrailway.gov.in
Waltair	drmwat@eastcoastrailway.gov.in
NR 	gm@nr.railnet.gov.in	Delhi	drm@dli.railnet.gov.in
Ambala	drm@umb.railnet.gov.in
Moradabad	drm@mb.railnet.gov.in
Lucknow	drm@lko.railnet.gov.in
Ferozepur	drm@fzr.railnet.gov.in
NCR    	gm@ncr.railnet.gov.in  	Allahabad	drm@ald.railnet.gov.in
Jhansi	drm@jhs.railnet.gov.in
Agra	drm@agc.railnet.gov.in
NER	gm@ner.railnet.gov.in	Izzatnagar	drmizn@ner.railnet.gov.in
Lucknow	drmljn@ner.railnet.gov.in
Varanasi	drmbsb@ner.railnet.gov.in
NFR	gm@nfr.railnet.gov.in	Katihar	drmkir@nfr.railnet.gov.in
Alipurduar	drmapdj@nfr.railnet.gov.in
Tinsukhia	drmtsk@nfr.railnet.gov.in
Lumding	drmlmg@nfr.railnet.gov.in
Rangia	drmrny@nfr.railnet.gov.in
NWR	gm@nwr.railnet.gov.in	Jaipur	drmjp@nwr.railnet.gov.in
Ajmer	drmaii@nwr.railnet.gov.in
Bikaner	drmbkn@nwr.railnet.gov.in
Jodhpur	drmju@nwr.railnet.gov.in
SR	gm@sr.railnet.gov.in	Chennai	drmmas@sr.railnet.gov.in
Madurai	drmmdu@sr.railnet.gov.in
Salem	drmsa@sr.railnet.gov.in
Palghat	drmpgt@sr.railnet.gov.in
Tiruchirapalli	drmtpj@sr.railnet.gov.in
Trivandrum	drmtvc@sr.railnet.gov.in
SCR	gm@scr.railnet.gov.in	Secundrabad	drmsc@scr.railnet.gov.in
Hyderabad	drmshyb@scr.railnet.gov.in
Guntkal	drmgtl@scr.railnet.gov.in
Guntur	drmgnt@scr.railnet.gov.in
Nanded	drmned@scr.railnet.gov.in
Vijayawada	drmbza@scr.railnet.gov.in"""