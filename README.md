# py-ao3list
## Work metadata scraper for AO3 (Archive of Our Own)

very early in development, there's probably a lot of things that shouldn't be here

the plan is to make this a package on PyPI

hopefully i do this right, and not accidentally make a tool that bothers ao3 servers...

the premise is to make a cli/tui tool that lets users keep track of what they read or something
uses python requests and beautifulsoup to get work metadata, right now it only includes title, creator, # of chapters, published date, and updated date
with that metadata, it will also store the work id and the last chapter read (although the user has to give the latter manually, i'm not going to make a tool that snoops on your browser)
probably could get other stats in, but the only ones i thought were important were the ones listed
keep in mind that this is NOT a reader, you do not read works using this

(way, way) future: make it a gui, as a lot of people (99% of normal people) generally don't use a terminal

if you have a problem with my work here (or don't), feel free to contact me: [liambragg1@gmail.com](mailto:liambragg1+pyao3list@gmail.com)

also feel free to make issues if you have suggestions!