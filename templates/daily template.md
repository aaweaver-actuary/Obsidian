
```dataviewjs
// set your own minimum year and the path to your journals (if applicable)
const minYear = 2023;
const journalPath = 'daily';

const rangeOfYears = (start, end) => Array(end - start + 1)
  .fill(start)
  .map((year, index) => year + index)
const d = moment();
const currentYear = d.year();
const availableYears = rangeOfYears(minYear, currentYear);
const month = ("0" + (d.month() + 1)).slice(-2);
const day = ("0" + (d.date())).slice(-2);
const dateString = month + '-' + day;

availableYears.forEach((y) => {
	let note = dv.page(`${journalPath}/${y}-${dateString})`);
	if (note) {
		dv.el('span', `[[${note.file.path}|${y}]] `);
	}
});
```



