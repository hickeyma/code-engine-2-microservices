# code-engine-2-microservices

## Scope

This repository is the code for the part 3 of the Code Engine YouTube series I've created.

## Usage

The first directory is [`node-true`](./node-true) which is the simple `nodejs`
application that defaults to returning a `'setting'` as `true`.

```bash
cd node-true
docker build -t node-true .
docker run -it -p 8080:8080 node-true
open localhost:8080
```

The second directory is [`python-get-quote`](./python-get-quote), which is the application
that will check the state of `node-true` then if is set correctly it will pull a
random quote from <https://zenquotes.io/>.

You'll need to set the `ENV` variable of `UPSTREAM` to the nodejs application. If
you're testing it locally it should default to `http://localhost:8080`.

```bash
curl -X GET https://zenquotes.io/api/random # to verify the quote API is woring
```

Building the container:

```bash
cd python-get-quote
docker build -t python-get-quote .
docker run -it -p 8081:8080 python-get-quote
open localhost:8081
```

## License & Authors

If you would like to see the detailed LICENCE click [here](./LICENCE).

- Author: JJ Asghar <awesome@ibm.com>

```text
Copyright:: 2021- IBM, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

