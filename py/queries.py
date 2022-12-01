#custom
QUERY_LAUNCHES = """{
  launches {
    id
    launch_date_local
    launch_success
    launch_year
    mission_id
    mission_name
    rocket {
      rocket {
        id
      }
    }
    ships {
      id
    }
  }
}
"""

#custom
QUERY_LINKS = """{
  launches {
    id
    links {
      article_link
      mission_patch
      reddit_campaign
      reddit_launch
      reddit_media
      reddit_recovery
      wikipedia
    }
  }
}
"""

#custom
QUERY_HISTORIES = """{
  histories {
    flight {
      id
    }
    title
    links {
      article
      reddit
      wikipedia
    }
  }
}
"""

#no custom
QUERY_MISSIONS="""{
  missions {
    
    id
    manufacturers
    name
    website
    wikipedia
  }
}
"""

#no custom
QUERY_ROCKETS = """{
  rockets {
    id
    name
    type
    company
  }
}
"""