// Databricks notebook source
def requestFormatter(givenTweet:String):String={
    s"""{
       "documents":[
        {
        "language":"en",
        "id":1,
        "text":"${givenTweet}"
        }
      ]
     }"""
}
  
def sendPostRequest(textAnalyticsUrl:String,subscriptionKey:String,requestBody:String):String={
  import scalaj.http.Http
  Thread.sleep(3000)
  val result = Http(textAnalyticsUrl).postData(requestBody)
  .header("Content-Type", "application/json")
  .header("Ocp-Apim-Subscription-Key", subscriptionKey).asString
  result.body
}

def removeHttpLines(textLine:String):Boolean={
  import scala.util.matching.Regex
  val pattern = "^http".r
  pattern.findFirstIn(textLine) match {
    case Some(x)=>false
    case _ => true
  }
}

val tweetsSentimentRdd =
sc.textFile("/google_access_tweets.txt").filter(removeHttpLines).map(x=>requestFormatter(x)).map(y=>sendPostRequest("https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment","1637a57b99cf43a0aeae9d72d2db7a1c",y))
val tweetsSentimentList = tweetsSentimentRdd.collect()
