# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2
import json
STUDENTS = [
  "Chad Solum",
  "Illa Mccormack",
  "Carol Burk",
  "Margarite Defilippo",
  "Sheryl Schwindt",
  "Coleman Salvia",
  "Despina Mathieu",
  "Chase Montalvo",
  "Caroll Wellman",
  "Lacey Blake",
  "Whelan Zhivago",
  "Jina Beringer",
  "Alysia Greenlee",
  "Steven Strange",
  "Kum Baggett",
  "Halina Bosco",
  "Angelita Voris",
  "Tiera Stalls",
  "Zac Efron",
  "Leontine Vandiver",
  "Devin Leahy",
  "Leisa Bumpus",
  "Mark Unicorn",
  "Yolande Briones",
  "Margart Oliphant",
  "Tawanda Patti",
  "Sparkle Musselman",
  "Ayana Welborn",
  "Justine Luebke"
]
def get_students(prefix):
  results = []
  if len(prefix) == 0:
    return results
  for student in STUDENTS:
    if student.lower().startswith(prefix.lower()):
      results.append(student)
      if len(results) == 5:
        return results
  return results
class StudentsHandler(webapp2.RequestHandler):
    def get(self):
      prefix = self.request.get('q')
      students = get_students(prefix)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.write(json.dumps(students))

app = webapp2.WSGIApplication([
    ('/students', StudentsHandler),
], debug=True)
