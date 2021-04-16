import twint

config = twint.Config()
config.Search = "bitcoin"
config.Limit = 10

twint.run.Search(config)
