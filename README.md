# cwpy
Crawler in Python

## Example (API POST)
```
{  
   "path":[  
      {  
         "id":"login_get",
         "url":"http:\/\/site-web-example\/login",
         "method":"GET",
         "get_inputs":[  
            {  
               "name":"token",
               "value":""
            }
         ],
         "return":"N"
      },
      {  
         "id":"login_post",
         "url":"http:\/\/site-web-example\/login",
         "method":"POST",
         "inputs":{  
            "login":"root",
            "password":"12345678",
            "token":{  
               "id_path":"login_get",
               "field":"token"
            }
         },
         "return":"N"
      },
      {  
         "id":"report",
         "url":"http:\/\/site-web-example\/page\/report",
         "method":"POST",
         "inputs":{  
            "type":"1",
            "date_start":"2018-10-01",
            "date_end":"2018-10-12"
         },
         "return":"Y"
      }
   ]
}
```