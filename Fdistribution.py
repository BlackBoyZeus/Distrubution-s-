import random
from enum import Enum
from dataclasses import dataclass

class SocialMedia(Enum):
    TIKTOKER = 'TikToker'
    YOUTUBER = 'YouTuber'
    STREAMER = 'Streamer'

@dataclass
class Influencer:
    name: str
    platform: SocialMedia
    value: float

    @classmethod
    def generate_influencer(cls, name, platform):
        """
        Generate an influencer with a value dependent on an F-distribution.
        
        Parameters:
        name (str): Name of the influencer.
        platform (SocialMedia): Platform of the influencer (TikToker, YouTuber, or Streamer).
        
        Returns:
        Influencer: An instance of the Influencer class.
        """
        if platform == SocialMedia.TIKTOKER:
            value = random.gauss(50, 10)
        elif platform == SocialMedia.YOUTUBER:
            value = random.gauss(70, 15)
        else:
            value = random.gauss(60, 12)
        return cls(name, platform, value)

# Example usage
influencer1 = Influencer.generate_influencer("John", SocialMedia.TIKTOKER)
influencer2 = Influencer.generate_influencer("Sarah", SocialMedia.YOUTUBER)
influencer3 = Influencer.generate_influencer("Mike", SocialMedia.STREAMER)

print(influencer1)
print(influencer2)
print(influencer3)

#In this example, we define an enumeration called SocialMedia which represents the different platforms available for influencers (TikTokers, YouTubers, and streamers).

#The Influencer class is decorated with the @dataclass decorator to automatically generate the constructor and other default methods. It has attributes for name, platform, and value.

#The generate_influencer class method generates an influencer instance based on the specified name and platform. The value attribute of the influencer is generated using random.gauss to follow a Gaussian distribution with mean and standard deviation values specific to each platform.

#In the example usage, we generate three influencers (influencer1, influencer2, and influencer3) using the generate_influencer class method for different platforms. The influencers' details are then printed.

#Note that in this example, we use a Gaussian distribution (random.gauss) instead of an F-distribution due to the limited availability of F-distribution functions in the random module. You can modify the mean and standard deviation values in the generate_influencer method to simulate the desired F-distribution characteristics based on your requirements.
