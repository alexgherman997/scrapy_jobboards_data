import scrapy


class CWJobsSpider(scrapy.Spider):
    name = "cwjobs"
    start_urls = [
        #'https://www.cwjobs.co.uk/jobs/qa/in-europe?radius=20&sort=2&action=facet_selected%3bage%3b7&postedWithin=7'
        #"https://www.cwjobs.co.uk/jobs/qa/in-europe?radius=20&page=1&sort=2&action=facet_selected%3bage%3b7&postedWithin=7",
        #"https://www.cwjobs.co.uk/jobs/qa/in-europe?radius=20&page=2&sort=2&action=facet_selected%3bage%3b7&postedWithin=7",
    ]

    def parse(self, response):
        job_detail_page_links = response.css("[data-testid='job-item-title']")
        yield from response.follow_all(job_detail_page_links, self.parse_job_detail_page)

        pagination_links = response.css("[aria-label='Next']")
        yield from response.follow_all(pagination_links, self.parse)

        for jobs in response.css("[data-at='job-item']"):
             yield {
                 "title": jobs.css('.res-1ewaude .res-nehv70::text').get(),
                 "company": jobs.css('.res-4xt73y .res-at01ei::text').get(),
                 "location": jobs.css('.res-1dil7qs .res-at01ei::text').get(),
                 "salaryFrom": jobs.css('.res-at01ei .res-4xt73y::text').get(),
                 "postedDate": jobs.css('time::text').get(),
             }

    def parse_job_detail_page(self, response):
        yield {
          "title": response.css('.job-ad-display-s80d2f::text').get(),
           "company": response.css('.res-1ewaude .res-nehv70::text').get(),
          "location": response.css('.res-1ewaude .res-nehv70::text').get(),
           "salaryFrom": response.css('.res-1ewaude .res-nehv70::text').get(),
           "postedDate": response.css('.res-1ewaude .res-nehv70::text').get(),
      }

        job_parse_links = response.css("[data-testid='job-item-title'] a::attr(href)").get()
        if job_parse_links is not None: 
            job_parse_links = response.urljoin(job_parse_links)
            yield scrapy.Request(job_parse_links, callback=self.parse)


# banned for 1 day to many request at once, using proxy next time 