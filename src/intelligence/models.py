class CompanyProfile:
    def __init__(self, name, industry, country, notes):
        self.name = name
        self.industry = industry
        self.country = country
        self.notes = notes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Company name cannot be empty")
        self._name = value.strip()

    def to_dict(self):
        return {
            "name": self._name,
            "industry": self.industry,
            "country": self.country,
            "notes": self.notes,
        }

    def summary(self):
        return f"""
    Company: {self._name}
    Industry: {self.industry}
    Country: {self.country}
    Notes: {self.notes}"""
