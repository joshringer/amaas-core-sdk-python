from __future__ import absolute_import, division, print_function, unicode_literals

from amaascore.assets.asset import Asset


class Equity(Asset):

    def __init__(self, asset_manager_id, asset_id, share_class='Common', asset_issuer_id=None, asset_status='Active',
                 issue_date=None, description='', country_id=None, venue_id=None,
                 links=None, references=None, *args, **kwargs):
        if not hasattr(self, 'asset_class'):  # A more specific child class may have already set this
            self.asset_class = 'Equity'
        self.share_class = share_class
        super(Equity, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id, fungible=True,
                                     asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                     description=description, country_id=country_id, venue_id=venue_id,
                                     links=links, references=references, issue_date=issue_date,
                                     *args, **kwargs)
