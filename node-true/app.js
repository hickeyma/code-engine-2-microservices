'use strict;'

const express = require('express')
const app = express()
const port = 8080

app.get('/', (req, res) => {

	  res.json({
			setting: true
		})
})

app.listen(port, () => {
	  console.log(`Example app listening at http://localhost:${port}`) 
})
