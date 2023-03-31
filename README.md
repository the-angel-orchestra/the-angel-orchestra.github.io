## How to...

### 1. Update the programme for future concerts

Add details to [the spreadsheet](https://docs.google.com/spreadsheets/d/1DvKwUS4tHe2646Fu8e1ut5JCUD-nd3AKn3TfUTI7EuI/edit?usp=sharing):

- date should be formatted as `day month year` (with day as a number without "th" etc and month as a word) for standard concerts or `day and day month year` for weekend workshops
- title and optional description, which can render html and is useful for providing details of weekend workshops and more complex scenarios e.g. when there is more than one soloist to mention
- for only one soloist, the subsequent columns can be used to display their name, an optional url to link out to from their name, and an optional description of their role (e.g. Soprano)
- programme details go in next, one piece per column
- either or both of venue and start_time can be: 
    - n/a to avoid clutter for future concerts 
    - left blank to display the default values of `Saint Silas Church on Risinghill Street, N1 9UL` and `5pm`
    - over-written with any other values
- ticket_info does not have a default value so if left blank nothing will appear here

Once the spreadsheet is up-to-date, log in to GitHub, navigate to [the Actions tab](https://github.com/the-angel-orchestra/the-angel-orchestra.github.io/actions) in the website repository, click on `CI` in the left-hand navigation bar, then click on `Run workflow` towards the right of the page, then the green `Run workflow` button (assuming `Branch: main` is selected in the dropdown that appears). This will launch the process of updating the website, which usually takes a couple of minutes to complete.

### 2. Update rehearsals information

Log in to GitHub and navigate to [the Code tab](https://github.com/the-angel-orchestra/the-angel-orchestra.github.io) of the website repository (which should appear by default).

In the directories listed in the centre of the screen, select `_includes` then `rehearsals.html`. 

You should now be looking at the text that appears in the middle of the [reheasals page](https://www.the-angel-orchestra.co.uk/rehearsals/) - click on the pen logo near the top right of your screen to edit directly in your browser as required (selecting "Soft wrap" from the drop-down that appears in place of the pen logo may make it easier to see all the text at once) then click the green `Commit changes` button at the bottom of the screen. This will launch the process of updating the website, which usually takes a couple of minutes to complete.

### 3. Update sheet music links

Most terms, we provide two categories of links to sheet music:

1. Parts that can be found on ISMLP. To add/edit these, log in to GitHub and navigate to [the Code tab](https://github.com/the-angel-orchestra/the-angel-orchestra.github.io) of the website repository, click on `_includes` and then `imslp.html`, then the pen logo to edit. Search IMSLP for the right urls then each piece needs to be added as a "list item" (or "li"), in the following format: `<li><a href="IMSLP_URL_HERE">PIECE_NAME_HERE</a></li>`, e.g. `<li><a href="https://imslp.org/wiki/Symphony_No.9%2C_Op.125_(Beethoven%2C_Ludwig_van)">Beethoven 9</a></li>`
2. Bowed parts - documentation to do!
